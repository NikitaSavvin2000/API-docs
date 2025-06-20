import streamlit as st
import pandas as pd
import os


cwd = os.getcwd()

path_to_example = os.path.join(cwd, "src", "examples", "example_1.csv")

st.title("🛠 Документация Horizon API")

st.markdown("""
### Описание

### 📈 POST https://nikitasavvin2000-horizon-api-921e.twc1.net/horizon_api

Генерация прогноза временного ряда на основе исторических данных.

---

## 📝 Описание

Этот эндпоинт позволяет получить прогноз временного ряда на основе переданного DataFrame. Алгоритм производит нормализацию данных, расширяет временной интервал до указанной точки в будущем и формирует прогноз целевой переменной.

---

""")

df = pd.read_csv(path_to_example)

st.write(f"## Пример файла")

st.write(df)

st.markdown("""
## 📥 Входные параметры

Тело запроса должно быть JSON-объектом следующей структуры:

```json
{
  "df": [...],
  "time_column": "time",
  "col_target": "load_consumption",
  "forecast_horizon_time": "2022-09-10 05:55:00"
}
```

| Поле | Тип | Обязательный | Описание |
|------|-------|----|----------|
| `df` | `List[Dict]` | ✅ | Исторические данные временного ряда в формате списка словарей (эквивалент `DataFrame.to_dict(orient="records")`). |
| `time_column` | `str` | ✅ | Название колонки с временными метками. |
| `col_target` | `str` | ✅ | Название целевой переменной, по которой строится прогноз. |
| `forecast_horizon_time` | `str` (в формате `YYYY-MM-DD HH:MM:SS`) | ✅ | Конечная дата прогноза, до которой необходимо построить значения. |

---

## 📤 Ответ

Успешный ответ (`200 OK`) содержит JSON-объект с предсказанными значениями.

```json
{
  "predictions": [
    {"time": "2022-09-10 05:10:00", "load_consumption": 123.45},
    {"time": "2022-09-10 05:15:00", "load_consumption": 124.01},
    ...
  ]
}
```

---

## ⚠️ Возможные ошибки

| Код | Описание |
|-----|----------|
| `502` | Ошибка при отправке запроса на внутреннюю модель (например, проблема сети). |
| `500` | Неизвестная внутренняя ошибка. Дополнительная информация передается в заголовке `X-Error`. |

---

## 🧪 Пример вызова на Python

```python
import requests
import pandas as pd

def func_generate_forecast(df: pd.DataFrame, time_column: str, col_target: str, forecast_horizon_time: str):
    url = "http://your_backend_url/backend/v1/generate_forecast"

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
            print(f"Ошибка при запросе: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

df = pd.read_csv("<your_data.csv>")
df["time"] = pd.to_datetime(df["time"])

response = func_generate_forecast(
    df=df,
    time_column="time",
    col_target="load_consumption",
    forecast_horizon_time="2022-09-10 05:00:00"
)
```

## 🧩 Дополнительно

- Убедитесь, что значения в `time_column` отсортированы по времени.
- Формат даты должен быть совместим с ISO 8601: `YYYY-MM-DD HH:MM:SS`.
- Прогноз будет построен от последней временной точки в `df` до `forecast_horizon_time`.

""")