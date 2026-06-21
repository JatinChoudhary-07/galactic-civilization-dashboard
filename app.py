
import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Galactic Civilization Dashboard",
    layout="wide"
)

# =========================
# IMPORTS
# =========================

from utils.loader import load_data
from utils.lore import get_lore
from utils.theme import load_theme

from components.sidebar import render_sidebar
from components.status import render_status
from components.metrics import render_metrics
from components.planet_image import render_planet_image
from components.charts import render_charts
from components.rankings import render_rankings
from components.comparison import render_comparison
from components.pdf_export import create_pdf


# =========================
# LOAD STYLES
# =========================

with open("styles/main.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# =========================
# LOAD DATA
# =========================

df = load_data()


# =========================
# SIDEBAR CONTROLS
# =========================

selected_planet, selected_year, theme = render_sidebar(df)

load_theme(theme)


# =========================
# FILTER DATA
# =========================

filtered_df = df[
    (df["planet"] == selected_planet)
    &
    (df["year"] == selected_year)
]

planet_history = df[
    df["planet"] == selected_planet
]

row = filtered_df.iloc[0]


# =========================
# SIDEBAR STATUS
# =========================

render_status(row)


# =========================
# HEADER
# =========================

st.caption(
    f"Viewing {selected_planet} • Year {selected_year}"
)

st.markdown(
    """
    <h1 class="main-title">
        Galactic Civilization Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================
# METRICS
# =========================

render_metrics(
    filtered_df,
    planet_history
)


# =========================
# PDF EXPORT
# =========================

pdf_file = create_pdf(
    selected_planet,
    row
)

st.download_button(
    "Download Planet Report",
    pdf_file,
    file_name=f"{selected_planet}_report.pdf",
    mime="application/pdf"
)

st.divider()


# =========================
# PLANET INTELLIGENCE
# =========================

st.subheader("Planet Intelligence")

left_col, right_col = st.columns([1, 2])

with left_col:

    render_planet_image(selected_planet)

    st.subheader(selected_planet)

    st.caption(
        "Monitoring interstellar civilization development"
    )

    st.write(
        get_lore(selected_planet)
    )

with right_col:

    render_charts(
        planet_history,
        theme
    )

st.divider()


# =========================
# GALACTIC RANKINGS
# =========================

render_rankings(
    df,
    theme
)

st.divider()


# =========================
# PLANET COMPARISON
# =========================

render_comparison(df)

