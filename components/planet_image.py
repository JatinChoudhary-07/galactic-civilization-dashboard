import streamlit as st

def render_planet_image(selected_planet):
    planet_images = {
        "Earth Prime": "assets/planets/earth_prime.png",
        "Nova Terra": "assets/planets/nova_terra.png",
        "Titania": "assets/planets/titania.png",
        "Aether": "assets/planets/aether.png",
        "Zorax": "assets/planets/zorax.png"
    }

    image_path = planet_images[selected_planet]

    st.image(
        image_path,
        width=300,
        caption=selected_planet
    )