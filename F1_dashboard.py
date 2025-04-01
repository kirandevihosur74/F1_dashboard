import streamlit as st

st.set_page_config(layout="wide")
st.title("🏎️ Formula 1 Insights Dashboard")

st.markdown("""
<iframe src="https://public.tableau.com/views/F1_dashboard_new/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
        width="1200" height="1000" frameborder="0"></iframe>
""", unsafe_allow_html=True)

