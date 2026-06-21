import streamlit as st

def render_status(row):

    st.sidebar.divider()

    st.sidebar.markdown("### Current Status")

    st.sidebar.metric(
        "Technology",
        row["technology"]
    )

    st.sidebar.metric(
        "Happiness",
        row["happiness"]
    )

    st.sidebar.divider()

    st.sidebar.markdown("### Civilization Status")

    status = []

    if row["technology"] > 130:
        status.append("Technological Boom")

    if row["happiness"] < 60:
        status.append("Social Unrest")

    if row["military"] > 100:
        status.append("Militarized")

    if not status:
        status.append("Stable")

    for item in status:
        st.sidebar.success(item)