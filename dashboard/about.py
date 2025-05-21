import streamlit as st

def show_about():
    st.title("About Dashboard App")
    st.markdown("""
    **Smart Flight** Dashboard App developed to help users predict flight ticket prices from Jakarta using the *Prophet* model and other data science techniques.

    **Current Features:**
    - 7-day ticket price prediction for popular destinations
    - Price range and uncertainty visualization

    **Next Features:**
    - Ticket price classification (cheap/medium/expensive)
    - Best time to buy ticket recommendation system
    - Promo price alerts or notifications

    Created by Defrizal Yahdiyan Risyad
    """)