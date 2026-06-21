import streamlit as st
import plotly.graph_objects as go



def render_comparison(df):

    st.subheader("Planet Comparison")

    planets = sorted(df["planet"].unique())

    selected = st.multiselect(
        "Choose planets",
        planets,
        default=planets[:2]
    )

    if len(selected) < 2:
        st.info("Select at least 2 planets")
        return

    comparison_df = (
        df[df["planet"].isin(selected)]
        .sort_values("year")
    )

    latest = (
        comparison_df
        .groupby("planet")
        .tail(1)
    )

    st.dataframe(
        latest[
            [
                "planet",
                "population",
                "economy",
                "military",
                "technology",
                "happiness"
            ]
        ],
        use_container_width=True
    )

    metrics = [
    "population",
    "economy",
    "military",
    "technology",
    "happiness"
]

    fig = go.Figure()

    for _, row in latest.iterrows():

        fig.add_trace(
            go.Scatterpolar(
                r=[row[m] for m in metrics],
                theta=[
                    "Population",
                    "Economy",
                    "Military",
                    "Technology",
                    "Happiness"
                ],
                fill="toself",
                name=row["planet"]
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 150]
            )
        ),
        showlegend=True,
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )