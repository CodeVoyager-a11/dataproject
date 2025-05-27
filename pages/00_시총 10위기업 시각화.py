import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import streamlit as st

st.title("글로벌 시총 상위 10개 기업 주가 시각화")

# 시총 10위 기업 티커 리스트
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM"
}

# 기간 설정 (최근 1년)
start_date = "2024-05-01"
end_date = "2025-05-01"

# Streamlit 멀티셀렉트로 기업 선택
selected_companies = st.multiselect("기업 선택", list(tickers.keys()), default=list(tickers.keys()))

if selected_companies:
    fig = go.Figure()
    
    for company in selected_companies:
        ticker = tickers[company]
        try:
            df = yf.download(ticker, start=start_date, end=end_date)
            if df.empty:
                st.warning(f"{company} 데이터가 없습니다.")
                continue
            
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df['Adj Close'],
                mode='lines',
                name=company
            ))
        except Exception as e:
            st.error(f"{company} 데이터를 불러오는 중 오류 발생: {e}")

    fig.update_layout(
        title="주가 조정 종가 (Adjusted Close) 추이",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("적어도 하나의 기업을 선택하세요.")
