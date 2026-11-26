from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Reach × Snowflake workshop", page_icon=":material/ac_unit:", layout="wide")

# The guide is a self-contained HTML page (inline CSS/JS, no external requests).
st.iframe(Path(__file__).parent / "guide.html", height="content", alt="Reach × Snowflake workshop guide")
