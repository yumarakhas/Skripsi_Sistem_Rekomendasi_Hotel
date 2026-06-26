from components.loader import load_data, resolve_best, _file_mtimes
from components.styles import inject_css, navbar
from components import section_params, section_grid, section_model, section_prediction
import os
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Evaluasi Sistem Rekomendasi",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# ── Styles & navbar ────────────────────────────────────────────────────────
inject_css()
navbar()

# ── Load data ──────────────────────────────────────────────────────────────
df_grid, df_comp, df_pred, metadata = load_data(DATA_DIR, _file_mtimes(DATA_DIR))

if df_grid is None:
    st.error(
        f"File `hasil_grid_search_K_alpha.csv` tidak ditemukan di folder `{DATA_DIR}`. "
        "Jalankan notebook dan pastikan cell penyimpanan hasil sudah dieksekusi."
    )
    st.stop()

best_k, best_alpha, best_rmse, best_mae = resolve_best(df_grid, metadata)

# ── Sections ───────────────────────────────────────────────────────────────
section_params.render_dataset_stats(metadata, df_grid)
section_params.render_best_params_with_table(best_k, best_alpha, best_rmse, best_mae, df_grid)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

section_grid.render(df_grid, best_k, best_alpha, best_rmse, best_mae)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

section_model.render(df_comp)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

section_prediction.render(df_pred)

# ── Footer ─────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="page-footer">'
    'Dashboard Evaluasi &mdash; Sistem Rekomendasi Hotel Hybrid (Word2Vec + KNN User-Based)'
    '</div>',
    unsafe_allow_html=True,
)
