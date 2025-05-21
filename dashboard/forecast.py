import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objs as go

def show_forecast():
    st.title("Flight Ticket Price Forecast from Jakarta")
    available_models = ['SUB', 'DPS', 'BDO', 'YIA', 'UPG', 'KNO', 'SRG', 'PKU', 'PDG', 'BPN']
    selected_dest = st.selectbox("Select Destination", available_models)

    model_path = f"../models/predict_popular_ticket/prophet_model_{selected_dest}.pkl"
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)
        forecast_7 = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=forecast_7['ds'], y=forecast_7['yhat'], name='Forecast'))
        fig.add_trace(go.Scatter(x=forecast_7['ds'], y=forecast_7['yhat_upper'], name='Upper Bound', line=dict(width=0)))
        fig.add_trace(go.Scatter(x=forecast_7['ds'], y=forecast_7['yhat_lower'], name='Lower Bound',
                                 fill='tonexty', fillcolor='rgba(173,216,230,0.3)', line=dict(width=0)))

        fig.update_layout(title=f'7 Days Ticket Price Forecast {selected_dest}',
                          xaxis_title='Date',
                          yaxis_title='Price (Rp)',
                          height=500)
        st.plotly_chart(fig)
        st.subheader("Forecast Tabel")
        st.dataframe(forecast_7.round(2))

    except FileNotFoundError:
        st.error(f"Model for purpose {selected_dest} not available.")
