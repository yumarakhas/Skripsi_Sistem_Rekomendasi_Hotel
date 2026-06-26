import plotly.graph_objects as go
import streamlit as st

CHART_LAYOUT = dict(
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(family="Inter, sans-serif", size=12, color="#000000"),
    margin=dict(t=48, l=16, r=16, b=16),
    title_font=dict(family="Space Grotesk, sans-serif", size=14, color="#000000"),
)


def render(df_pred):
    st.markdown(
        '<div class="section-hd">'
        '  <span class="section-title">Hasil Prediksi Rating</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    if df_pred is None:
        st.warning(
            "File `hasil_prediksi_hybrid_best.csv` belum ditemukan di folder data."
        )
        return

    st.markdown(
        f'<p style="font-size:0.85rem;color:#64748B;margin-bottom:0.75rem;">'
        f'Menampilkan <strong>{len(df_pred):,}</strong> data prediksi rating '
        f'dari model hybrid terbaik.</p>',
        unsafe_allow_html=True,
    )

    # ── Hitung distribusi error ────────────────────────────────────────────
    total = len(df_pred)
    ae = df_pred["Absolute Error"]
    n_low = int((ae < 0.5).sum())
    n_mid = int(((ae >= 0.5) & (ae < 1.0)).sum())
    n_high = int((ae >= 1.0).sum())
    p_low = n_low / total * 100
    p_mid = n_mid / total * 100
    p_high = n_high / total * 100

    # ── Dua kolom: tabel (kiri) & chart (kanan) ───────────────────────────
    col_table, col_chart = st.columns([3, 2], gap="medium")

    with col_table:
        DISPLAY_ROWS = 100
        html_table = df_pred.head(DISPLAY_ROWS).to_html(
            index=False, classes="scroll-table", border=0
        )
        st.markdown(
            f'<div class="scroll-table-wrap">{html_table}</div>',
            unsafe_allow_html=True,
        )
        if len(df_pred) > DISPLAY_ROWS:
            st.caption(
                f"Menampilkan {DISPLAY_ROWS} dari {len(df_pred):,} data prediksi."
            )

    with col_chart:
        labels = ["< 0,5", "0,5 – < 1,0", "≥ 1,0"]
        values = [p_low, p_mid, p_high]
        colors = ["#10B981", "#F59E0B", "#EF4444"]

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=labels,
                y=values,
                marker_color=colors,
                marker_line_width=0,
                text=[f"{v:.1f}%" for v in values],
                textposition="outside",
                textfont=dict(
                    size=12, color="#000000", family="Space Grotesk, sans-serif"
                ),
                width=0.5,
            )
        )
        fig.update_layout(
            **CHART_LAYOUT,
            title="Distribusi Akurasi Prediksi",
            xaxis=dict(
                title="Rentang Absolute Error",
                showgrid=False,
                zeroline=False,
                tickfont=dict(color="#000000"),
                title_font=dict(color="#000000"),
            ),
            yaxis=dict(
                title="Persentase (%)",
                showgrid=True,
                gridcolor="#F1F5F9",
                zeroline=False,
                tickfont=dict(color="#000000"),
                title_font=dict(color="#000000"),
                range=[0, max(values) * 1.2],
            ),
            bargap=0.3,
            height=450,
        )
        st.plotly_chart(fig, use_container_width=True)
