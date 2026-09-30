import os
import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題與佈局
st.set_page_config(
    page_title="多彩線上思維導圖 (Supabase 共創版)",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隱藏 Streamlit 預設邊距與外框，實現滿版顯示
st.markdown("""
    <style>
        .block-container { padding: 0rem; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# 動態取得 app.py 當前所在的完整資料夾路徑，解決子資料夾找不到 index.html 的問題
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

# 讀取同目錄下的 index.html 檔案內容
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# 將 HTML 心智圖應用嵌入至 Streamlit 頁面中 (高度設定為 920px)
components.html(html_content, height=920, scrolling=False)
