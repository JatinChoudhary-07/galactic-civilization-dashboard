
import streamlit as st


def render_sidebar(df):

    # Theme Toggle
    theme = st.sidebar.toggle(
        "Light Mode",
        value=False
    )

    st.sidebar.title("Navigation")

    # Planet List
    planets = sorted(
        df["planet"].unique()
    )

    # Planet Search
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

    # Planet Selector
    selected_planet = st.sidebar.selectbox(
        "Select Planet",
        planets
    )

    # Year Selector
    selected_year = st.sidebar.selectbox(
        "Select Year",
        sorted(
            df["year"].unique()
        )
    )

    return (
        selected_planet,
        selected_year,
        theme
    )

