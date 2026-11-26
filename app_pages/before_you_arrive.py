import streamlit as st

st.title("Before you arrive")

with st.container(border=True):
    st.subheader(":material/laptop_mac: Everyone")
    st.checkbox("Laptop with a current Chrome, Edge or Safari", key="p_laptop")
    st.checkbox("Can sign in to Reach's Snowflake account (SSO/MFA working)", key="p_sf")
    st.checkbox("GitHub account with access to the workshop repository", key="p_gh")

with st.container(border=True):
    st.subheader(":material/admin_panel_settings: Snowflake and GitHub admins")
    st.markdown(
        "- Workshop roles, warehouse and databases created\n"
        "- Python packages (Anaconda terms) enabled for the account\n"
        "- Empty workshop repository in Reach's GitHub organization\n"
        "- GitHub Actions and the Snowflake GitHub App allowed for that repository"
    )
    st.caption("Setup scripts and a short checklist will be shared with admins ahead of the session.")

st.info("Questions before the session? Contact your Snowflake account team.", icon=":material/help:")
