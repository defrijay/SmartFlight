import streamlit as st

def show_home():
    st.markdown("""
    **Smart Flight** is a dashboard application for analyzing flight ticket price data from Jakarta to various cities in Indonesia.

    ### Key Features:
    - 🔮 Flight ticket price prediction for the next 7 days
    - 📊 Visualization of price range and uncertainty *(coming soon)*
    - 🧠 Ticket price classification *(coming soon)*
    - 🎯 Best time to buy recommendation *(coming soon)*

    Start by selecting the menu on the left. 👈
    """)
    st.image("https://cdn.pixabay.com/photo/2016/03/09/15/10/airplane-1245746_1280.jpg", caption="Smart Flight - Forecast Your Ticket", use_column_width=True)
