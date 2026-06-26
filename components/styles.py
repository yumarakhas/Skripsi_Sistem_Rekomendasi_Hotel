import streamlit as st


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Force white background */
        .stApp,
        .main,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"] {
            background-color: #FFFFFF !important;
        }

        /* Hide Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="collapsedControl"] { display: none; }

        /* Page layout */
        .main .block-container {
            padding: 1.5rem 2.5rem 3rem 2.5rem !important;
            max-width: 1200px !important;
        }

        /* ── Navbar ── */
        .navbar {
            background: #0F2D6B;
            padding: 0.75rem 2.5rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
        }
        .navbar-brand {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.95rem;
            font-weight: 600;
            color: #FFFFFF;
            line-height: 1.4;
        }
        .navbar-sub {
            font-size: 0.72rem;
            color: #93C5FD;
            font-weight: 400;
            margin-top: 0.1rem;
        }

        /* ── Stat cards ── */
        .stat-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.875rem;
            margin-bottom: 1.75rem;
        }
        .stat-card {
            background: #FFFFFF;
            border-radius: 10px;
            padding: 1rem 1.25rem;
            border: 1px solid #E2E8F0;
            border-left: 4px solid #1D4ED8;
        }
        .stat-card.green { border-left-color: #0D9488; }
        .stat-card.amber { border-left-color: #B45309; }
        .stat-card.navy  { border-left-color: #0F2D6B; }
        .stat-label {
            font-size: 0.68rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            color: #64748B;
            margin-bottom: 0.3rem;
        }
        .stat-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            color: #0F2D6B;
            line-height: 1;
        }

        /* ── Param cards ── */
        .param-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.875rem;
            margin-bottom: 1.25rem;
        }
        .param-card {
            background: #0F2D6B;
            border-radius: 10px;
            padding: 1rem 1.25rem;
        }
        .param-card.light {
            background: #F8FAFF;
            border: 1px solid #DBEAFE;
        }
        .param-label {
            font-size: 0.68rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            color: #93C5FD;
            margin-bottom: 0.3rem;
        }
        .param-card.light .param-label { color: #3B82F6; }
        .param-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            color: #FFFFFF;
            line-height: 1;
        }
        .param-card.light .param-value { color: #0F2D6B; }

        /* ── Section header ── */
        .section-hd {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin: 1.75rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #DBEAFE;
        }
        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: #0F2D6B;
            margin: 0;
        }
        .section-pill {
            font-size: 0.65rem;
            font-weight: 600;
            color: #1D4ED8;
            background: #DBEAFE;
            border-radius: 999px;
            padding: 0.15rem 0.6rem;
        }

        /* ── Table (st.dataframe) — border hitam ── */
        [data-testid="stDataFrame"] {
            border: 1px solid #000000;
            border-radius: 0;
            overflow: hidden;
        }
        [data-testid="stDataFrame"] [data-testid="glideDataEditor"] {
            border-color: #000000 !important;
        }

        /* ── Table (st.table) — putih, garis hitam, teks hitam ── */
        [data-testid="stTable"],
        [data-testid="stTable"] > div,
        [data-testid="stTable"] table,
        .stTable,
        .stTable table {
            background-color: #FFFFFF !important;
            border-collapse: collapse !important;
            width: 100% !important;
            border-radius: 0 !important;
            overflow: visible !important;
        }
        [data-testid="stTable"] th,
        .stTable th {
            background-color: #F1F5F9 !important;
            color: #1E293B !important;
            border: 1px solid #000000 !important;
            padding: 0.5rem 0.75rem !important;
            font-weight: 600 !important;
            text-align: center !important;
        }
        [data-testid="stTable"] td,
        .stTable td {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            padding: 0.5rem 0.75rem !important;
        }

        /* ── Scrollable table (sama tema dengan st.table) ── */
        .scroll-table-wrap {
            max-height: 450px;
            overflow-y: auto;
            border: none;
            border-radius: 0;
        }
        .scroll-table {
            background-color: #FFFFFF;
            border-collapse: separate;
            border-spacing: 0;
            width: 100%;
            font-size: 0.85rem;
        }
        .scroll-table thead th {
            position: sticky;
            top: 0;
            z-index: 10;
            background-color: #F1F5F9;
            color: #1E293B;
            border-right: 1px solid #000000;
            border-top: none;
            border-bottom: none;
            padding: 0.5rem 0.75rem;
            font-weight: 600;
            white-space: nowrap;
            text-align: center;
            box-shadow:
                inset 0  1px 0 #000000,
                inset 0 -1px 0 #000000,
                      0  1px 0 #000000;
        }
        .scroll-table thead th:first-child {
            border-left: 1px solid #000000;
        }
        .scroll-table tbody td {
            background-color: #FFFFFF;
            color: #000000;
            border-bottom: 1px solid #000000;
            border-right: 1px solid #000000;
            padding: 0.5rem 0.75rem;
        }
        .scroll-table tbody td:first-child {
            border-left: 1px solid #000000;
        }
        /* scrollbar — hanya pill biru, tanpa rail/kotak */
        .scroll-table-wrap {
            overflow-y: overlay;
            scrollbar-width: thin;
            scrollbar-color: #1D4ED8 transparent;
        }
        .scroll-table-wrap::-webkit-scrollbar {
            width: 6px;
            background: transparent;
        }
        .scroll-table-wrap::-webkit-scrollbar-track {
            background: transparent;
        }
        .scroll-table-wrap::-webkit-scrollbar-button {
            display: none;
            height: 0;
        }
        .scroll-table-wrap::-webkit-scrollbar-thumb {
            background: #1D4ED8;
            border-radius: 99px;
        }
        .scroll-table-wrap::-webkit-scrollbar-thumb:hover {
            background: #0F2D6B;
        }

        /* ── Chart ── */
        [data-testid="stPlotlyChart"] {
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            overflow: hidden;
        }

        /* ── Divider ── */
        .soft-divider {
            border: none;
            border-top: 1px solid #E2E8F0;
            margin: 1.5rem 0;
        }

        /* ── Radio — default style, lingkaran navy saat selected ── */
        [data-testid="stRadio"] > label {
            color: #000000 !important;
            font-weight: 600 !important;
        }
        [data-testid="stRadio"] > div {
            flex-direction: row;
            gap: 0.5rem;
        }
        /* Teks label hitam */
        [data-testid="stRadio"] label p,
        [data-testid="stRadio"] label span {
            color: #000000 !important;
            background: transparent !important;
        }
        /* Lingkaran radio — selected jadi navy */
        [data-testid="stRadio"] [role="radiogroup"] > label[data-checked="true"] > div:first-child {
            background-color: #0F2D6B !important;
            border-color: #0F2D6B !important;
        }

        /* ── Tabs — teks hitam, selected navy ── */
        [data-testid="stTabs"] [role="tab"] {
            color: #000000 !important;
            font-weight: 500;
        }
        [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
            color: #0F2D6B !important;
            font-weight: 600;
        }

        /* ── Caption/info grafik — hitam ── */
        .stCaption, [data-testid="stCaptionContainer"] {
            color: #000000 !important;
        }

        /* ── Footer ── */
        .page-footer {
            margin-top: 2.5rem;
            padding-top: 1rem;
            border-top: 1px solid #E2E8F0;
            font-size: 0.75rem;
            color: #94A3B8;
            line-height: 1.6;
        }
        /* ── Info cards (side-by-side) ── */
        .info-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            height: 100%;
        }
        .info-card-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            color: #0F2D6B;
            margin-bottom: 0.85rem;
        }
        .info-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.82rem;
        }
        .info-table th {
            text-align: left;
            font-weight: 600;
            color: #64748B;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.5rem 0.75rem;
            border-bottom: 2px solid #E2E8F0;
        }
        .info-table td {
            padding: 0.6rem 0.75rem;
            color: #1E293B;
            border-bottom: 1px solid #F1F5F9;
        }
        .info-table tbody tr:last-child td {
            border-bottom: none;
        }

        /* ── Badges ── */
        .badge {
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            white-space: nowrap;
        }
        .badge-green {
            background: #D1FAE5;
            color: #065F46;
        }
        .badge-amber {
            background: #FEF3C7;
            color: #92400E;
        }
        .badge-red {
            background: #FEE2E2;
            color: #991B1B;
        }

        /* ── Horizontal bar chart ── */
        .bar-row {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin-bottom: 0.75rem;
        }
        .bar-row:last-child { margin-bottom: 0; }
        .bar-label {
            font-size: 0.8rem;
            font-weight: 600;
            color: #1E293B;
            min-width: 90px;
            flex-shrink: 0;
        }
        .bar-track {
            flex: 1;
            height: 22px;
            background: #F1F5F9;
            border-radius: 6px;
            overflow: hidden;
        }
        .bar-fill {
            height: 100%;
            border-radius: 6px;
            transition: width 0.6s ease;
        }
        .bar-green { background: #10B981; }
        .bar-amber { background: #F59E0B; }
        .bar-red   { background: #EF4444; }
        .bar-pct {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.82rem;
            font-weight: 700;
            color: #0F2D6B;
            min-width: 45px;
            text-align: right;
            flex-shrink: 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def navbar():
    st.markdown(
        """
        <div class="navbar">
            <div class="navbar-brand">
                Sistem Rekomendasi Hotel &mdash; Hybrid Filtering (Word2Vec + KNN)
            </div>
            <div class="navbar-sub">
                Dataset: Kaggle &nbsp;&bull;&nbsp; Mustafa Harashi
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
