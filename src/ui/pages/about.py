import streamlit as st

if "lang" not in st.session_state:
    st.session_state.lang = "ru"

TEXTS = {
    "ru": """
# 📈 API для прогнозирования временных рядов

Прогнозирование временных рядов — это не просто расчет будущих значений.  
Это сложный процесс, включающий:

- очистку и нормализацию данных  
- выбор и настройку моделей  
- учет сезонности, трендов, выбросов  
- валидацию результатов  
- работу с множеством метрик и критериев

🧩 Всё это требует времени, экспертизы и выстроенного пайплайна.

---

Мы упростили всё это до одного действия: **вызова нашей API-ручки**.

Теперь вам не нужно собирать систему по частям — всё уже встроено в наше решение:

- 📊 интеллектуальный выбор модели  
- 🧠 машинное обучение  
- 🔄 автоматическая обработка временных рядов  
- 📦 единый вход — готовый прогноз на выходе

Передайте исходные данные — и получите прогноз. Всё просто.

---

🎯 **Сконцентрируйтесь на принятии решений. Прогнозы мы берём на себя.**
""",
    "en": """
# 📈 Time Series Forecasting API

Time series forecasting isn’t just about projecting future values.  
It’s a complex process that includes:

- data cleaning and normalization  
- model selection and tuning  
- handling seasonality, trends, and outliers  
- validating the results  
- managing multiple metrics and evaluation criteria

🧩 All of this takes time, expertise, and a reliable pipeline.

---

We’ve simplified it to a single action: **calling our API endpoint**.

You no longer need to piece together your forecasting system — everything is built-in:

- 📊 intelligent model selection  
- 🧠 machine learning  
- 🔄 automated time series processing  
- 📦 one input — ready-to-use forecast output

Just send your raw data — and receive the forecast. That’s it.

---

🎯 **Focus on decisions. Let us handle the forecast.**
""",
    "zh": """
# 📈 时间序列预测 API

时间序列预测不仅仅是预测未来的数值。  
它是一个复杂的流程，包括：

- 数据清洗与标准化  
- 模型选择与调参  
- 处理季节性、趋势和异常值  
- 结果验证  
- 使用多种评估指标和标准

🧩 这一切都需要经验、时间和稳定的流程。

---

我们把这一切简化为一个操作：**调用我们的 API 接口**。

无需再拼凑各种工具，一切已为你准备好：

- 📊 智能模型选择  
- 🧠 机器学习支持  
- 🔄 自动处理时间序列  
- 📦 单一输入 — 即可获得预测结果

你只需要传入原始数据，即可获得预测结果。如此简单！

---

🎯 **专注于业务决策，预测交给我们。**
"""
}

st.markdown(TEXTS[st.session_state.lang])
