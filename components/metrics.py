import streamlit as st


def get_growth(metric, row, planet_history):

    current_year = row["year"]

    current = row[metric]

    current_index = planet_history[
        planet_history["year"] == current_year
    ].index[0]

    history_indices = list(planet_history.index)

    position = history_indices.index(current_index)

    if position == 0:
        return "0.0%"

    previous_value = planet_history.iloc[position - 1][metric]

    growth = (
        (current - previous_value)
        / previous_value
    ) * 100

    return f"{growth:.1f}%"


def render_metrics(filtered_df, planet_history):

    row = filtered_df.iloc[0]

    metrics = [
        ("Population", "population"),
        ("Economy", "economy"),
        ("Military", "military"),
        ("Technology", "technology"),
        ("Happiness", "happiness")
    ]

    cols = st.columns(5)

    for col, (label, metric) in zip(cols, metrics):

        col.metric(
            label,
            row[metric],
            get_growth(metric, row, planet_history)
        )