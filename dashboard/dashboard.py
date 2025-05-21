import streamlit as st
from home import show_home
from forecast import show_forecast
from classification import show_classification
from recommendation import show_recommendation
from about import show_about

# =================== Inisialisasi halaman aktif ===================
if "page" not in st.session_state:
    st.session_state.page = "HomePage"

def set_page(page_name):
    st.session_state.page = page_name

# =================== Header ===================
st.markdown("""
    <div style='background-color:#4a90e2;padding:10px;border-radius:10px'>
        <h1 style='color:white;text-align:center;'>✈️ Smart Flight Dashboard</h1>
    </div>
""", unsafe_allow_html=True)

# =================== Sidebar ===================
st.sidebar.title("Navigation")
st.sidebar.button("🏠 Homepage", on_click=set_page, args=("HomePage",))
st.sidebar.button("📈 Price Forecasting", on_click=set_page, args=("PriceForecasting",))
st.sidebar.button("💰 Price Classification", on_click=set_page, args=("PriceClassification",))
st.sidebar.button("🎯 Recommendation", on_click=set_page, args=("Recommendation",))
st.sidebar.button("ℹ️ About", on_click=set_page, args=("About",))

# =================== Routing ===================
page = st.session_state.page
if page == "HomePage":
    show_home()
elif page == "PriceForecasting":
    show_forecast()
elif page == "PriceClassification":
    show_classification()
elif page == "Recommendation":
    show_recommendation()
elif page == "About":
    show_about()