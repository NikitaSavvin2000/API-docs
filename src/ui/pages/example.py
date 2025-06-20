import streamlit as st

st.set_page_config(page_title="📈 Пример использования API для прогноза", layout="wide")

st.title("📈 Пример функции для генерации прогноза")
st.markdown("""
Это пример Python-функции, которая отправляет DataFrame с временным рядом на backend API  
и получает прогноз на указанный горизонт времени.

""")
st.markdown("### 🔗 [Полный рабочий пример в Google Colab](https://colab.research.google.com/drive/1jdo3EBuHgpBtvp0xsFXIGFDQOidWlCRa?usp=sharing)")


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
