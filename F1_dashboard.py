import streamlit as st

st.set_page_config(layout="wide")
st.title("🏎️ Formula 1 Insights Dashboard")
st.markdown(
    """
    <iframe src="https://public.tableau.com/views/F1_dashboard_new/Dashboard2?:embed=y&:display_count=yes&:showVizHome=no"
            width="1400" height="1400" frameborder="0" style="border:none;"></iframe>
    """,
    unsafe_allow_html=True
)
