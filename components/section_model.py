import plotly.graph_objects as go
import streamlit as st

CHART_LAYOUT = dict(
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(family="Inter, sans-serif", size=12, color="#000000"),
    margin=dict(t=48, l=16, r=16, b=16),
    title_font=dict(family="Space Grotesk, sans-serif", size=14, color="#000000"),
)


def render(df_comp):
    st.markdown(
        '<div class="section-hd">'
        '  <span class="section-title">Perbandingan Antar Model</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    if df_comp is None:
        st.warning(
            "File `hasil_perbandingan_model.csv` belum ditemukan di folder data. "
            "Tambahkan kode penyimpanan perbandingan model di notebook."
        )
        return

    fig_bar = go.Figure()
    fig_bar.add_trace(
        go.Bar(
            x=df_comp["Model"],
            y=df_comp["RMSE"],
            name="RMSE",
            marker_color="#0F2D6B",
            marker_line_width=0,
            text=df_comp["RMSE"].round(4),
            textposition="outside",
            textfont=dict(size=11, color="#000000"),
        )
    )
    fig_bar.add_trace(
        go.Bar(
            x=df_comp["Model"],
            y=df_comp["MAE"],
            name="MAE",
            marker_color="#60A5FA",
            marker_line_width=0,
            text=df_comp["MAE"].round(4),
            textposition="outside",
            textfont=dict(size=11, color="#000000"),
        )
    )
    fig_bar.update_layout(
        **CHART_LAYOUT,
        barmode="group",
        bargap=0.28,
        bargroupgap=0.08,
        title="User-Based KNN vs Content-Based (Word2Vec) vs Hybrid",
        xaxis_title="Metode",
        yaxis_title="Nilai Error",
        legend_title="Metrik",
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color="#000000"), title_font=dict(color="#000000")),
        yaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False, tickfont=dict(color="#000000"), title_font=dict(color="#000000")),
        legend=dict(font=dict(color="#000000"), title_font=dict(color="#000000")),
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown(
        '<p style="font-size:0.8rem;font-weight:600;color:#64748B;'
        'text-transform:uppercase;letter-spacing:0.05em;margin:1rem 0 0.5rem 0;">'
        'Tabel Perbandingan Model</p>',
        unsafe_allow_html=True,
    )
    st.table(df_comp)
