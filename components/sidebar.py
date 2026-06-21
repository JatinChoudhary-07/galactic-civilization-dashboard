import streamlit as st

def render_sidebar(df):

    theme = st.sidebar.toggle(
    "Light Mode",
    value=False
    )
    
    planets = sorted(
    df["planet"].unique()
    )
    search_query = st.sidebar.text_input(
        "Search Planet"
    )
    if search_query:

        planets = [
            planet
            for planet in planets
            if search_query.lower()
            in planet.lower()
        ]

    st.sidebar.title("Navigation")
    selected_planet = st.sidebar.selectbox(
        "Select Planet",
        planets
    )
    

    selected_year = st.sidebar.selectbox(
        "Select Year",
        sorted(df["year"].unique())
    )

    return selected_planet, selected_year, theme