import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(page_title="글로벌 시총 10대 기업 주가 추이", layout="wide")

st.title("🌍 글로벌 시가총액 상위 10개 기업 주가 시각화")
st.markdown("""
이 앱은 야후 파이낸스 데이터를 기반으로, 세계 시가총액 상위 10개 기업의 최근 주가 추이를 보여줍니다.
""")

# 시총 상위 10개 기업 및 티커
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK.B",
    "Meta Platforms": "META",
    "TSMC": "TSM"
}

# --- 사이드바 ---
st.sidebar.header("🔧 설정")
selected_companies = st.sidebar.multiselect(
    "기업 선택", list(tickers.keys()), default=list(tickers.keys())
)

# 날짜 범위 선택
end_date = datetime.today()
start_date = st.sidebar.date_input(
    "시작 날짜", end_date - timedelta(days=365), min_value=datetime(2000, 1, 1), max_value=end_date - timedelta(days=1)
)

# --- 본문 내용 ---
if not selected_companies:
    st.warning("📌 최소 하나 이상의 기업을 선택해주세요.")
else:
    fig = go.Figure()

    for company in selected_companies:
        ticker = tickers[company]
        try:
            df = yf.download(ticker, start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"), progress=False)
            if df.empty:
                st.warning(f"⚠️ {company} ({ticker}) 데이터가 없습니다.")
                continue

            fig.add_trace(go.Scatter(
                x=df.index,
                y=df['Adj Close'],
                mode='lines',
                name=company
            ))

        except Exception as e:
            st.error(f"❌ {company} 데이터 로드 중 오류: {e}")

    fig.update_layout(
        title="📈 주가 조정 종가 (Adjusted Close) 추이",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
