planet_lore = {
    "Earth Prime": "Birthplace of humanity and the political center of the galaxy.",

    "Nova Terra": "A rapidly growing colony world driven by innovation and commerce.",

    "Titania": "A harsh volcanic world known for military strength and resource extraction.",

    "Aether": "A technologically advanced gas giant colony with floating cities.",

    "Zorax": "A mysterious frontier world rich in ancient alien artifacts."
}

def get_lore(planet):
    return planet_lore.get(
        planet,
        "No information available"
    )
