import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

CHART_LAYOUT = dict(
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(family="Inter, sans-serif", size=12, color="#000000"),
    margin=dict(t=48, l=16, r=16, b=16),
    title_font=dict(family="Space Grotesk, sans-serif", size=14, color="#000000"),
)

# 10 warna kontras untuk 10 nilai K — biru-hijau-teal yang mudah dibedakan
NAVY_PALETTE = [
    "#0F2D6B",  # K=3  navy gelap
    "#1D4ED8",  # K=4  biru tua
    "#2563EB",  # K=5  biru
    "#3B82F6",  # K=6  biru medium
    "#60A5FA",  # K=7  biru muda
    "#0D9488",  # K=8  teal gelap
    "#14B8A6",  # K=9  teal
    "#7C3AED",  # K=10 ungu
    "#B45309",  # K=11 amber tua
    "#DC2626",  # K=12 merah
]


def render(df_grid, best_k, best_alpha, best_rmse, best_mae):
    st.markdown(
        '<div class="section-hd">'
        '  <span class="section-title">Perbandingan Parameter Antar Percobaan (K x Alpha)</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    metric_choice = st.radio("Metrik:", ["RMSE", "MAE"], horizontal=True)

    tab_line, tab_heatmap = st.tabs(["Line Chart per K", "Heatmap K x Alpha"])

    with tab_line:
        plot_df = df_grid.sort_values(["K", "alpha"])
        plot_df = plot_df.copy()
        plot_df["K"] = plot_df["K"].astype(str)  # pastikan K sebagai string untuk warna diskrit

        k_vals = sorted(df_grid["K"].unique())
        color_map = {str(k): NAVY_PALETTE[i % len(NAVY_PALETTE)] for i, k in enumerate(k_vals)}

        fig_line = px.line(
            plot_df,
            x="alpha",
            y=metric_choice,
            color="K",
            markers=True,
            labels={"alpha": "Alpha (bobot KNN)", metric_choice: metric_choice, "K": "K"},
            title=f"{metric_choice} vs Alpha untuk Setiap Nilai K",
            color_discrete_map=color_map,
        )
        fig_line.update_traces(line_width=2, marker_size=6)
        fig_line.add_vline(
            x=best_alpha,
            line_dash="dot",
            line_color="#94A3B8",
            line_width=1.5,
            annotation_text=f"α={best_alpha}",
            annotation_font_size=11,
            annotation_font_color="#000000",
        )
        fig_line.add_trace(
            go.Scatter(
                x=[best_alpha],
                y=[best_rmse if metric_choice == "RMSE" else best_mae],
                mode="markers",
                marker=dict(
                    size=14,
                    color="#F59E0B",
                    symbol="star",
                    line=dict(width=1.5, color="#0F2D6B"),
                ),
                name=f"Terbaik (K={best_k}, α={best_alpha:.1f})",
            )
        )
        fig_line.update_layout(
            **CHART_LAYOUT,
            legend_title="K",
            xaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False, tickfont=dict(color="#000000"), title_font=dict(color="#000000")),
            yaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False, tickfont=dict(color="#000000"), title_font=dict(color="#000000")),
            legend=dict(font=dict(color="#000000"), title_font=dict(color="#000000")),
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with tab_heatmap:
        pivot = df_grid.pivot(index="K", columns="alpha", values=metric_choice)

        # Bangun teks tiap sel — tambahkan bintang langsung di teks sel terbaik
        text_matrix = []
        for i, k_val in enumerate(pivot.index):
            row = []
            for j, a_val in enumerate(pivot.columns):
                val = pivot.iloc[i, j]
                if int(k_val) == int(best_k) and abs(float(a_val) - float(best_alpha)) < 1e-9:
                    row.append(f"{val:.4f} ⭐")
                else:
                    row.append(f"{val:.4f}")
            text_matrix.append(row)

        fig_heat = go.Figure(data=go.Heatmap(
            z=pivot.values,
            x=[str(c) for c in pivot.columns],
            y=[str(r) for r in pivot.index],
            text=text_matrix,
            texttemplate="%{text}",
            textfont=dict(size=10),
            colorscale=[[0, "#DBEAFE"], [0.5, "#2563EB"], [1, "#0F2D6B"]],
            colorbar=dict(thickness=12, len=0.8, title=metric_choice),
            hovertemplate="K=%{y}<br>Alpha=%{x}<br>" + metric_choice + "=%{z:.4f}<extra></extra>",
        ))
        alpha_labels = [str(c) for c in pivot.columns]
        k_labels = [str(r) for r in pivot.index]
        fig_heat.update_xaxes(
            title_text="Alpha", side="bottom",
            type="category",
            categoryorder="array",
            categoryarray=alpha_labels,
            tickfont=dict(size=11, color="#000000"),
            title_font=dict(color="#000000"),
        )
        fig_heat.update_yaxes(
            title_text="K",
            type="category",
            categoryorder="array",
            categoryarray=k_labels,
            tickfont=dict(size=11, color="#000000"),
            title_font=dict(color="#000000"),
        )

        fig_heat.update_layout(
            **CHART_LAYOUT,
            title=f"Heatmap {metric_choice} — Grid Search (K x Alpha)",
        )
        st.plotly_chart(fig_heat, use_container_width=True)
        st.caption(f"✨ Nilai {metric_choice} terendah: K={best_k}, Alpha={best_alpha:.1f}.")
