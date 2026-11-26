from pathlib import Path

import streamlit as st

# Add or edit Markdown files in content/ to publish instructions.
CONTENT = Path(__file__).parent.parent / "content"

st.title("Instructions")
st.markdown((CONTENT / "instructions.md").read_text())
