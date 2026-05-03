import streamlit as st
from data import incident, signals, dependencies, changes, tickets
from engine import reconstruct_context
from formatter import format_context

st.title("Context Lens")
st.caption("Reconstructing the story behind enterprise incidents")

if st.button("Analyze Incident"):

    context = reconstruct_context(
        incident,
        signals,
        dependencies,
        changes,
        tickets
    )

    output = format_context(context, incident)

    st.subheader("Context Thread")
    st.text(output)