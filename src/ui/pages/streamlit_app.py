import streamlit as st

LANGUAGES = {
    "🇷🇺 Русский (Россия)": "ru",
    "🇺🇸 English (USA)": "en",
    "🇨🇳 中文 (中国)": "zh"
}

if "lang" not in st.session_state:
    st.session_state.lang = "ru"

def change_lang():
    selected = st.session_state.lang_selector
    st.session_state.lang = LANGUAGES[selected]

current_key = [k for k, v in LANGUAGES.items() if v == st.session_state.lang][0]

st.sidebar.selectbox(
    "🌐 Выберите язык / Select Language",
    options=list(LANGUAGES.keys()),
    index=list(LANGUAGES.keys()).index(current_key),
    key="lang_selector",
    on_change=change_lang
)


about_page = st.Page("about.py", title="About", icon=":material/info:")
docs_page = st.Page("api_docs.py", title="Documentation", icon=":material/menu_book:")
example_page = st.Page("example.py", title="Examples", icon=":material/auto_awesome:")


pg = st.navigation([about_page, docs_page, example_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()