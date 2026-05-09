import streamlit as st

# 1. 페이지 설정 (가장 먼저 실행되어야 함)
st.set_page_config(page_title="Vibe Picker", page_icon="🖤", layout="centered")

# 2. 고정된 스타일링 (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    div.stButton > button {
        width: 100%;
        border-radius: 0px;
        border: 1px solid #000;
        background-color: white;
        color: black;
        height: 3em;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #000;
        color: #fff;
    }
    .vibe-card {
        padding: 20px;
        border: 1px solid #eee;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 세팅 (이미지 주소는 Unsplash 다이렉트 링크 사용)
data = {
    "Minimal Classic": {
        "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=800",
        "tag": "무채색의 정갈함, 셔츠와 슬랙스",
        "tip": "가죽 벨트 하나로 룩의 완성도를 높여보세요."
    },
    "Lovely Mood": {
        "img": "https://images.unsplash.com/photo-1554520735-0ad66a951bb8?auto=format&fit=crop&w=800",
        "tag": "셔링 디테일과 부드러운 파스텔 톤",
        "tip": "플랫 슈즈를 매치해 사랑스러움을 더하세요."
    },
    "Street Hip": {
        "img": "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=800",
        "tag": "오버핏 후드와 비니, 와이드 팬츠",
        "tip": "볼드한 실버 목걸이가 잘 어울려요."
    }
}

# 4. 앱 타이틀
st.markdown("<h2 style='text-align: center;'>Choose Your Vibe</h2>", unsafe_allow_html=True)
st.write("")

# 5. 버튼 레이아웃 (3열)
col1, col2, col3 = st.columns(3)

# 세션 상태 초기화 (처음 접속 시 첫 번째 데이터 표시)
if 'choice' not in st.session_state:
    st.session_state.choice = "Minimal Classic"

with col1:
    if st.button("미니멀"): st.session_state.choice = "Minimal Classic"
with col2:
    if st.button("러블리"): st.session_state.choice = "Lovely Mood"
with col3:
    if st.button("스트릿"): st.session_state.choice = "Street Hip"

st.divider()

# 6. 결과 표시 섹션
selected = st.session_state.choice
item = data[selected]

c1, c2 = st.columns([1, 1])

with c1:
    # use_column_width 대신 최신 버전인 use_container_width 사용
    st.image(item["img"], use_container_width=True)

with c2:
    st.markdown(f"### {selected}")
    st.write(f"**Key:** {item['tag']}")
    st.write("---")
    st.info(f"💡 {item['tip']}")

st.markdown("<p style='text-align:center; color:#ccc; margin-top:50px;'>Produced by Vibe Coding</p>", unsafe_allow_html=True)
