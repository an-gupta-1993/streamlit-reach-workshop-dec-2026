import streamlit as st

st.set_page_config(page_title="Reach × Snowflake workshop", page_icon=":material/ac_unit:", layout="wide")

page = st.navigation(
    [
        st.Page("app_pages/agenda.py", title="Agenda", icon=":material/event:", default=True),
        st.Page("app_pages/before_you_arrive.py", title="Before you arrive", icon=":material/checklist:"),
        st.Page("app_pages/instructions.py", title="Instructions", icon=":material/menu_book:"),
    ]
)
page.run()
