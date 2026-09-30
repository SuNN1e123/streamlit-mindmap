import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="多彩線上思維導圖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隱藏外圍邊距，滿版顯示
st.markdown("""
    <style>
        .block-container { padding: 0rem; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# 讀取 index.html 並嵌入頁面
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=920, scrolling=False)