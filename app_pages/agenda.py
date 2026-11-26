import pandas as pd
import streamlit as st

# Edit the agenda here. Times are local (MT).
SESSION = {
    "title": "From data to production on Snowflake",
    "date": "Tuesday, December 1, 2026",
    "time": "9:00 – 12:00 MT",
    "where": "Reach office · in person",
}

AGENDA = [
    {"start": "09:00", "end": "09:15", "block": "Welcome and setup check", "track": "Setup",
     "icon": ":material/login:", "detail": "Logins, roles and workspace ready."},
    {"start": "09:15", "end": "10:15", "block": "Explore and experiment", "track": "Hands-on",
     "icon": ":material/science:", "detail": "Notebooks in Workspaces, Snowpark, feature engineering, an anomaly model in Python."},
    {"start": "10:15", "end": "10:25", "block": "Break", "track": "Break",
     "icon": ":material/coffee:", "detail": ""},
    {"start": "10:25", "end": "10:55", "block": "Productionize", "track": "Hands-on",
     "icon": ":material/schedule:", "detail": "Notebook code becomes stored procedures, chained and scheduled as a task graph."},
    {"start": "10:55", "end": "11:30", "block": "Version and deploy", "track": "Hands-on",
     "icon": ":material/merge:", "detail": "Git from Workspaces, pull requests, GitHub Actions promoting DEV to PROD."},
    {"start": "11:30", "end": "11:50", "block": "AI on your pipeline", "track": "Hands-on",
     "icon": ":material/smart_toy:", "detail": "Cortex Search and a Cortex Agent that explain flagged payments."},
    {"start": "11:50", "end": "12:00", "block": "Wrap-up and next steps", "track": "Setup",
     "icon": ":material/flag:", "detail": "Questions and follow-ups."},
]

st.title(SESSION["title"])
with st.container(horizontal=True):
    st.badge(SESSION["date"], icon=":material/calendar_month:", color="blue")
    st.badge(SESSION["time"], icon=":material/schedule:", color="blue")
    st.badge(SESSION["where"], icon=":material/location_on:", color="gray")
st.caption("Draft agenda · subject to change")

# Timeline
df = pd.DataFrame(AGENDA)
day = "2026-12-01 "
df["start_ts"] = pd.to_datetime(day + df["start"])
df["end_ts"] = pd.to_datetime(day + df["end"])
df["minutes"] = ((df["end_ts"] - df["start_ts"]).dt.total_seconds() // 60).astype(int)

st.vega_lite_chart(
    df[["block", "track", "start_ts", "end_ts", "minutes"]],
    {
        "height": 260,
        "mark": {"type": "bar", "cornerRadius": 4},
        "encoding": {
            "y": {"field": "block", "type": "nominal", "sort": None, "title": None},
            "x": {"field": "start_ts", "type": "temporal", "title": None, "axis": {"format": "%H:%M"}},
            "x2": {"field": "end_ts"},
            "color": {"field": "track", "type": "nominal", "title": None, "legend": {"orient": "top"}},
            "tooltip": [
                {"field": "block", "title": "Block"},
                {"field": "start_ts", "type": "temporal", "format": "%H:%M", "title": "Start"},
                {"field": "minutes", "title": "Minutes"},
            ],
        },
    },
    alt="Agenda timeline from 9:00 to 12:00",
)

# Blocks
for item in AGENDA:
    with st.container(border=True, horizontal=True, vertical_alignment="center"):
        st.markdown(f"**{item['start']}–{item['end']}**", width=120)
        with st.container(gap="small"):
            st.markdown(f"{item['icon']} **{item['block']}**")
            if item["detail"]:
                st.caption(item["detail"])
