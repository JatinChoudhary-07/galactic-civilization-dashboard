import streamlit as st


def load_theme(light_mode):

    if light_mode:

        with open("styles/light.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    else:

        with open("styles/main.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )