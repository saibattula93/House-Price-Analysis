import streamlit as st
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


st.title("US House Price Analysis")

st.header("User Input")


spend = st.number_input("spend", min_value=0 ,value=353065)
permits = st.number_input("permits", min_value=0,  value=1277)
permit_val = st.number_input("permit_val", min_value=0.0,  value=998.312)
starts = st.number_input("starts", min_value=0,  value=1268)
completions = st.number_input("completions", min_value=0,  value=1262)
manufactured = st.number_input("manufactured", min_value=0,  value=304)
new_for_sale = st.number_input("new house for sale", min_value=0,  value=310)
months_supply = st.number_input("months supply", min_value=0.0,  value=4.3)
emratio = st.number_input("employement ratio", min_value=0.0,  value=64.6)
pop_level = st.number_input("population level", min_value=0,  value=211410)
gdp = st.number_input("GDP", min_value=0.0,  value=101.5179979)
mortgage_rate = st.number_input("mortgage_rate", min_value=0.0,  value=8.21)
fed_fund_rate = st.number_input("fed_fund_rate", min_value=0.0,  value=3.99)
disp_income = st.number_input("disp_income", min_value=0.0,  value=9309.1)
pm_save = st.number_input("pm_save", min_value=0.0,  value=358.9)
consump_durable = st.number_input("consump_durable", min_value=0.0,  value=908.6)
new_sold = st.number_input("new_sold", min_value=0,  value=873)
rent_vacancy = st.number_input("rent_vacancy", min_value=0.0,  value=7.90)
owner_vacancy = st.number_input("owner_vacancy", min_value=0.0,  value=1.60)
week_earning = st.number_input("week_earning", min_value=0.0,  value=603.00)
delinquent_rate = st.number_input("delinquent_rate", min_value=0.0,  value=1.95)
hor = st.number_input("hor", min_value=0.0,  value=67.1)
hp_idx_qtr = st.number_input("hp_idx_qtr", min_value=0.0,  value=101.33)




user_data = {
    "spend": spend,
    "permits": permits,
    "permit_val": permit_val,
    "starts": starts,
    "completions": completions,
    "manufactured": manufactured,
    "new_for_sale": new_for_sale,
    "months_supply": months_supply,
    "emratio": emratio,
    "pop_level": pop_level,
    "gdp": gdp,
    "mortgage_rate": mortgage_rate,
    "fed_fund_rate": fed_fund_rate,
    "disp_income": disp_income,
    "pm_save": pm_save,
    "consump_durable": consump_durable,
    "new_sold": new_sold,
    "rent_vacancy": rent_vacancy,
    "owner_vacancy": owner_vacancy,
    "week_earning": week_earning,
    "delinquent_rate": delinquent_rate,
    "hor": hor,
    "hp_idx_qtr" : hp_idx_qtr
}


# Function to make predictions
def predict_data(user_data):
    data = CustomData(
        spend=user_data["spend"],
        permits=user_data["permits"],
        permit_val=user_data["permit_val"],
        starts=user_data["starts"],
        completions=user_data["completions"],
        manufactured=user_data["manufactured"],
        new_for_sale=user_data["new_for_sale"],
        months_supply=user_data["months_supply"],
        emratio=user_data["emratio"],
        pop_level=user_data["pop_level"],
        gdp=user_data["gdp"],
        mortgage_rate=user_data["mortgage_rate"],
        fed_fund_rate=user_data["fed_fund_rate"],
        disp_income=user_data["disp_income"],
        pm_save=user_data["pm_save"],
        consump_durable=user_data["consump_durable"],
        new_sold=user_data["new_sold"],
        rent_vacancy=user_data["rent_vacancy"],
        owner_vacancy=user_data["owner_vacancy"],
        week_earning=user_data["week_earning"],
        delinquent_rate=user_data["delinquent_rate"],
        hor=user_data["hor"],
        hp_idx_qtr = user_data['hp_idx_qtr']
    )

    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    return results[0]



if st.button("Predict"):
    results = predict_data(user_data)
    st.subheader("Estimated Home Price Index in US:")
    st.info(f" {round(results, 2):,.2f}")


