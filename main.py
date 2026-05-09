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
        "tip": "볼드한 실버 목걸이가 잘 어울import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="Random Vibe Picker", page_icon="🎲", layout="centered")

# 2. 감각적인 미니멀 스타일링
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        border: 2px solid #000;
        background-color: #000;
        color: #fff;
        font-weight: bold;
        padding: 15px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #fff;
        color: #000;
    }
    .vibe-title { font-family: 'serif'; font-size: 40px; font-weight: bold; text-align: center; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 방대한 추구미 데이터베이스 (랜덤 소스)
vibe_db = [
    {"name": "Minimal Classic", "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105", "tag": "정갈함의 정석", "tip": "화이트 셔츠와 와이드 슬랙스 조합."},
    {"name": "Soft Romantic", "img": "https://images.unsplash.com/photo-1529133039941-e856b3629146", "tag": "사랑스러운 분위기", "tip": "파스텔 톤 가디건을 걸쳐보세요."},
    {"name": "Street Hipster", "img": "https://images.unsplash.com/photo-1509631179647-0177331693ae", "tag": "자유분방한 힙", "tip": "비니와 볼드한 체인 목걸이 추천."},
    {"name": "Quiet Luxury", "img": "https://images.unsplash.com/photo-1485968579580-b6d095142e6e", "tag": "우아한 소재감", "tip": "실크 스카프로 포인트를 주세요."},
    {"name": "Vintage Y2K", "img": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f", "tag": "세기말 감성", "tip": "로우라이즈 팬츠와 컬러풀한 집업."},
    {"name": "Gorpcore", "img": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3", "tag": "고기능성 아웃도어", "tip": "테크니컬 재킷과 고어텍스 슈즈."},
    {"name": "City Boy", "img": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b", "tag": "여유로운 실루엣", "tip": "오버사이즈 옥스퍼드 셔츠를 활용하세요."},
    {"name": "Office Siren", "img": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2", "tag": "지적인 섹시미", "tip": "뿔테 안경과 펜슬 스커트가 핵심."}
]

# 4. 앱 UI
st.markdown("<div class='vibe-title'>Pick Your Vibe</div>", unsafe_allow_html=True)

# 랜덤 버튼
if st.button("오늘의 추구미 랜덤 추출하기 🎲"):
    # 랜덤 선택
    result = random.choice(vibe_db)
    st.session_state.current_vibe = result
    st.balloons() # 축하 효과

# 결과 노출
if 'current_vibe' in st.session_state:
    item = st.session_state.current_vibe
    
    st.write("---")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # 고유 ID를 쿼리스트링으로 붙여 매번 새로운 느낌 연출
        st.image(f"{item['img']}?auto=format&fit=crop&w=800&q={random.randint(1,100)}", use_container_width=True)
        
    with col2:
        st.subheader(f"✨ {item['name']}")
        st.write(f"**Mood:** {item['tag']}")
        st.info(f"**Advice:** {item['tip']}")
        
        if st.button("한 번 더! 🔄"):
            st.rerun()
else:
    st.write("")
    st.info("위의 검정색 버튼을 눌러 오늘 당신의 스타일을 결정해보세요!")

# 5. 하단 장식
st.markdown("<br><br><p style='text-align: center; color: #eee;'>EVERYDAY IS YOUR RUNWAY</p>", unsafe_allow_html=True)
