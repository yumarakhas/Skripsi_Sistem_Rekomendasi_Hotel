import streamlit as st


def render_dataset_stats(metadata, df_grid):
    if not metadata:
        return

    # Hitung total data (test + train jika ada, atau n_test saja)
    n_test = metadata.get("n_test", 0)
    n_train = metadata.get("n_train", 0)
    total_data = n_test + n_train if n_train else n_test

    st.markdown(
        f"""
        <div class="stat-row" style="grid-template-columns: repeat(3, 1fr);">
            <div class="stat-card">
                <div class="stat-label">Total Data</div>
                <div class="stat-value">{total_data:,}</div>
            </div>
            <div class="stat-card green">
                <div class="stat-label">Jumlah User</div>
                <div class="stat-value">{metadata.get("n_user", "-"):,}</div>
            </div>
            <div class="stat-card amber">
                <div class="stat-label">Jumlah Hotel</div>
                <div class="stat-value">{metadata.get("n_hotel", "-"):,}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_best_params_with_table(best_k, best_alpha, best_rmse, best_mae, df_grid):
    st.markdown(
        '<div class="section-hd">'
        '  <span class="section-title">Parameter Terbaik</span>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="param-row">
            <div class="param-card">
                <div class="param-label">Best K (Jumlah Tetangga)</div>
                <div class="param-value">{best_k}</div>
            </div>
            <div class="param-card">
                <div class="param-label">Best Alpha (Bobot KNN)</div>
                <div class="param-value">{best_alpha:.1f}</div>
            </div>
            <div class="param-card light">
                <div class="param-label">RMSE</div>
                <div class="param-value">{best_rmse:.4f}</div>
            </div>
            <div class="param-card light">
                <div class="param-label">MAE</div>
                <div class="param-value">{best_mae:.4f}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tabel langsung tampil tanpa expander
    st.markdown(
        '<p style="font-size:0.8rem;font-weight:600;color:#64748B;'
        'text-transform:uppercase;letter-spacing:0.05em;margin:1rem 0 0.5rem 0;">'
        '10 Kombinasi Parameter Terbaik</p>',
        unsafe_allow_html=True,
    )
    st.table(
        df_grid.sort_values("RMSE").head(10).reset_index(drop=True),
    )
