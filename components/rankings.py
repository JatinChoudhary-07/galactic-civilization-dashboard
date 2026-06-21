import streamlit as st
import plotly.express as px

def render_rankings(df, theme):
    st.subheader("Galactic Rankings")

    col1, col2, col3 = st.columns(3)

    if theme:
        paper_bg = "#ffffff"
        font_color = "#111111"

    else:
        paper_bg = "#05080d"
        font_color = "white"
    
    
    rankings = [
        ("economy", "Economy"),
        ("technology", "Technology"),
        ("happiness", "Happiness")
    ]

    for col, (metric, title) in zip(
        [col1, col2, col3],
        rankings
    ):
        
        ranking_df = (
            df.groupby("planet")[metric]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        ranking_df["planet"] = [
        f"#{i+1} {planet}"
        for i, planet in enumerate(ranking_df["planet"])
        ]

        fig = px.bar(
            ranking_df,
            x=metric,
            y="planet",
            orientation="h"
        )

        fig.update_layout(
            title=title,
            height=350,
            margin=dict(l=10, r=10, t=40, b=10),
            yaxis=dict(
                categoryorder="total ascending"
            ),

        paper_bgcolor=paper_bg,
        plot_bgcolor=paper_bg,
        font=dict(color=font_color),
        )

        fig.update_traces(
            marker_color="#69ff7a"
        )

        col.plotly_chart(
            fig,
            use_container_width=True
        )
