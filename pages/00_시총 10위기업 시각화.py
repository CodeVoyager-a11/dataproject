import yfinance as yf
import plotly.graph_objs as go
import streamlit as st

st.title("글로벌 시총 상위 10개 기업 주가 시각화")

# 시총 10위 기업 티커 리스트 (BRK-B -> BRK.B)
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK.B",
    "Meta": "META",
    "TSMC": "TSM"
}

# 기간 설정 (최근 1년)
start_date = "2024-05-01"
end_date = "2025-05-01"

# 기업 선택 멀티셀렉트
selected_companies = st.multiselect("기업 선택", list(tickers.keys()), default=list(tickers.keys()))

if not s
