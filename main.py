import streamlit as st

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. 페이지 제목
st.title("서초구 학교 위치 지도")

# 2. 데이터 불러오기 (예시: 서울시 학교 위치 데이터)
@st.cache_data
def load_school_data():
    url = "https://raw.githubusercontent.com/your-repo/seochogu-schools/main/seochogu_schools.csv"
    return pd.read_csv(url)

df = load_school_data()

# 3. 서초구 필터링
seochogu_schools = df[df['주소'].str.contains('서초구')]

# 4. 지도 생성
m = folium.Map(location=[37.4836, 127.0326], zoom_start=13)

# 5. 마커 추가
for _, row in seochogu_schools.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=f"{row['학교명']} ({row['학교급'])}",
        tooltip=row['학교명']
    ).add_to(m)

# 6. 지도 출력
st.subheader("서초구 내 학교 위치")
st_folium(m, width=700, height=500)

