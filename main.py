import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 제목
st.title("서울 서초구 학교 위치 지도")

# 예시 데이터 생성 (샘플 CSV 대체)
data = {
    "학교명": ["서초초등학교", "반포중학교", "서초고등학교"],
    "학교급": ["초등학교", "중학교", "고등학교"],
    "주소": [
        "서울특별시 서초구 서초대로 1",
        "서울특별시 서초구 반포대로 2",
        "서울특별시 서초구 남부순환로 3"
    ],
    "위도": [37.4872, 37.5031, 37.4702],
    "경도": [127.0154, 127.0112, 127.0398]
}
df = pd.DataFrame(data)

# 지도 생성
m = folium.Map(location=[37.4836, 127.0326], zoom_start=13)

# 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=f"{row['학교명']} ({row['학교급']})",
        tooltip=row["학교명"]
    ).add_to(m)

# 지도 출력
st.subheader("🗺️ 서초구 학교 위치")
st_folium(m, width=700, height=500)
