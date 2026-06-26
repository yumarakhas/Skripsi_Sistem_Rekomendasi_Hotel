import json
import os

import pandas as pd
import streamlit as st


def _file_mtimes(data_dir: str) -> tuple:
    """Return modification timestamps of data files (used to bust cache)."""
    files = [
        "hasil_grid_search_K_alpha.csv",
        "hasil_perbandingan_model.csv",
        "hasil_prediksi_hybrid_best.csv",
        "metadata_userbased.json",
    ]
    mtimes = []
    for f in files:
        p = os.path.join(data_dir, f)
        mtimes.append(os.path.getmtime(p) if os.path.exists(p) else 0)
    return tuple(mtimes)


@st.cache_data
def load_data(data_dir: str, _mtimes: tuple = ()):
    grid_path = os.path.join(data_dir, "hasil_grid_search_K_alpha.csv")
    comp_path = os.path.join(data_dir, "hasil_perbandingan_model.csv")
    pred_path = os.path.join(data_dir, "hasil_prediksi_hybrid_best.csv")
    meta_path = os.path.join(data_dir, "metadata_userbased.json")

    df_grid = pd.read_csv(grid_path) if os.path.exists(grid_path) else None
    df_comp = pd.read_csv(comp_path) if os.path.exists(comp_path) else None

    df_pred = None
    if os.path.exists(pred_path):
        df_pred = pd.read_csv(
            pred_path,
            usecols=["user_id", "hotel_id", "actual", "predicted", "abs_error"],
        )
        df_pred = df_pred.rename(columns={
            "user_id": "User ID",
            "hotel_id": "Hotel ID",
            "actual": "Rating Aktual",
            "predicted": "Rating Prediksi",
            "abs_error": "Absolute Error",
        })

    metadata = None
    if os.path.exists(meta_path):
        with open(meta_path) as f:
            metadata = json.load(f)

    return df_grid, df_comp, df_pred, metadata


def resolve_best(df_grid, metadata):
    best_row   = df_grid.loc[df_grid["RMSE"].idxmin()]
    best_k     = int(metadata["best_k"])       if metadata else int(best_row["K"])
    best_alpha = float(metadata["best_alpha"]) if metadata else float(best_row["alpha"])

    match     = df_grid[(df_grid["K"] == best_k) & (df_grid["alpha"] == best_alpha)]
    best_rmse = float(match["RMSE"].values[0]) if len(match) else float(best_row["RMSE"])
    best_mae  = float(match["MAE"].values[0])  if len(match) else float(best_row["MAE"])

    return best_k, best_alpha, best_rmse, best_mae
