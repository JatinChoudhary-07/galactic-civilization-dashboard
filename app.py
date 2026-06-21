import streamlit as st

# =========================
# IMPORTS
# =========================

from utils.loader import load_data
from utils.lore import get_lore
from utils.theme import load_theme

from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.planet_image import render_planet_image
from components.charts import render_charts
from components.rankings import render_rankings
from components.comparison import render_comparison
from components.pdf_export import create_pdf

# Load custom CSS
with open("styles/main.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

    # =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Galactic Civilization Dashboard",
    layout="wide"
)

# =========================
# DATA LOADING
# =========================

# Load CSV into dataframe
df = load_data()


# =========================
# USER INPUTS
# =========================

# Get selected planet and year from sidebar
selected_planet, selected_year, theme = render_sidebar(df)

load_theme(theme)
# Keep only matching row
filtered_df = df[
    (df["planet"] == selected_planet)
    &
    (df["year"] == selected_year)
]
planet_history = df[
    df["planet"] == selected_planet
]

st.sidebar.divider()

st.sidebar.markdown("### Current Status")

st.sidebar.metric(
    "Technology",
    filtered_df["technology"].iloc[0]
)
st.sidebar.metric(
    "Happiness",
    filtered_df["happiness"].iloc[0]
)
st.sidebar.divider()

st.sidebar.markdown("### Civilization Status")

tech = filtered_df["technology"].iloc[0]
happy = filtered_df["happiness"].iloc[0]
military = filtered_df["military"].iloc[0]

status = []

if tech > 130:
    status.append("Technological Boom")

if happy < 60:
    status.append("Social Unrest")

if military > 100:
    status.append("Militarized")

if len(status) == 0:
    status.append("Stable")

for s in status:
    st.sidebar.success(s)

st.caption(
    f"Viewing {selected_planet} • Year {selected_year}"
)

# =========================
# PAGE CONTENT
# =========================

st.markdown(
    """
    <h1 class='main-title'>
        🌌 Galactic Civilization Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)
    

st.divider()


# Show civilization metrics
render_metrics(filtered_df,planet_history)
row = filtered_df.iloc[0]

pdf_file = create_pdf(
    selected_planet,
    row
)

st.download_button(
    "📄 Download Planet Report",
    pdf_file,
    file_name=f"{selected_planet}_report.pdf",
    mime="application/pdf"
)

st.divider()

st.subheader("Planet Intelligence")

left, right = st.columns([1, 2])

with left:

    render_planet_image(selected_planet)

    st.subheader(selected_planet)

    st.caption(
        "Monitoring interstellar civilization development"
    )

    st.write(get_lore(selected_planet))

with right:

    render_charts(planet_history, theme)

st.divider()

render_rankings(df, theme)

st.divider()

render_comparison(df)

