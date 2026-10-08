import streamlit as st

st.set_page_config(
    page_title="Mianus River Conditions",
    page_icon="🌊"
)

st.title("Mianus River Conditions")
st.write("Wind, weather, and tidal forecasts for the Mianus River.")

date = st.date_input("Select a date")
time = st.time_input("Select a time")

st.write(f"Selected forecast: {date} at {time}")