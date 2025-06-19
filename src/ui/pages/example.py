import streamlit as st

code = '''import pandas as pd
import requests

def func_generate_forecast(df: pd.DataFrame, time_column: str, col_target: str, forecast_horizon_time: str):
    url = f"{base_url}/generate_forecast"

    df_records = df.to_dict(orient='records')

    data = {
        "df": df_records,
        "time_column": time_column,
        "col_target": col_target,
        "forecast_horizon_time": forecast_horizon_time
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request exception occurred: {e}")
        return None
'''


st.code(code, language="python")