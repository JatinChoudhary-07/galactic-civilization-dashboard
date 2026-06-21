import streamlit as st
import plotly.express as px

def render_charts(planet_history, theme):
    if theme:
        paper_bg = "#ffffff"
        font_color = "#111111"

    else:
        paper_bg = "#05080d"
        font_color = "white"

    metric = st.selectbox(
        "Trend Metric",
        [
            "population",
            "economy",
            "military",
            "technology",
            "happiness"
        ]
    )

    fig = px.line(
        planet_history,
        x="year",
        y=metric,
        markers=True
    )

    fig.update_traces(
    line_color="#69ff7a",
    marker_color="#69ff7a",
    line_width=4,
    fill="tozeroy"
    )

    fig.update_layout(
    hovermode="x unified",
    paper_bgcolor=paper_bg,
    plot_bgcolor=paper_bg,
    font=dict(color=font_color),
    height=450
    )

    st.caption(
    f"{metric.title()} Trend"
    )   

    st.plotly_chart(
        fig,
        use_container_width=True
    )