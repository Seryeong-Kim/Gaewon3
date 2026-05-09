import streamlit as st
import random

# 세션 설정 및 페이지 디자인
st.set_page_config(page_title="Mood Picker", page_icon="✨", layout="centered")

# 커스텀 CSS: 미니멀한 감성을 위한 폰트 및 스타일링
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
        color: #333333;
    }
    .stButton>button {
        border-radius: 20px;
        border: 1px solid #eeeeee;
        background-color: white;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        border-color: #000000;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# 헤더 섹션
st.title("Today's Vibe ✨")
st.write("오늘 당신이 머물고 싶은 분위기를 선택하세요.")

# 데이터 정의: 추구미 스타일
styles = {
    "Minimal Classic": {
        "desc": "정갈한 셔츠, 잘 재단된 슬랙스, 그리고 화이트 톤.",
        "quote": "가장 단순한 것이 가장 아름답습니다.",
        "color": "#F5F5F5"
    },
    "Soft Grunge": {
        "desc": "오버사이즈 니트, 바랜 데님, 그리고 자유로운 레이어드.",
        "quote": "정해진 틀에서 조금은 벗어나도 괜찮아요.",
        "color": "#D3D3D3"
    },
    "Quiet Luxury": {
        "desc": "로고 없는 고급스러움, 뉴트럴 톤의 캐시미어와 실크.",
        "quote": "드러내지 않아도 느껴지는 견고한 취향.",
        "color": "#EAE0D5"
    },
    "Sporty Chic": {
        "desc": "바이커 쇼츠, 오버핏 블레이저, 그리고 깨끗한 스니커즈.",
        "quote": "움직임 속에서 발견하는 도심의 활기.",
        "color": "#E8F0FE"
    }
}

# 인터페이스: 버튼 배열
col1, col2 = st.columns(2)

selected_mood = None

with col1:
    if st.button("미니멀 클래식"):
        selected_mood = "Minimal Classic"
    if st.button("소프트 그렁지"):
        selected_mood = "Soft Grunge"

with col2:
    if st.button("콰이어트 럭셔리"):
        selected_mood = "Quiet Luxury"
    if st.button("스포티 시크"):
        selected_mood = "Sporty Chic"

st.divider()

# 결과 출력
if selected_mood:
    res = styles[selected_mood]
    st.subheader(f"Target Vibe: {selected_mood}")
    
    # 감각적인 카드 형태의 결과창
    st.info(f"**Style Cue:** {res['desc']}")
    st.write(f"> *{res['quote']}*")
    
    # 랜덤 팁 추가
    tips = ["볼드한 실버 링으로 포인트를 줘보세요.", "향수는 우디한 계열을 추천해요.", "헤어는 자연스러운 로우번 어때요?"]
    st.caption(f"💡 Suggestion: {random.choice(tips)}")

else:
    st.write("버튼을 눌러 오늘의 '추구미'를 확인하세요.")

# 푸터
st.markdown("<br><br><p style='text-align: center; color: #bfbfbf; font-size: 12px;'>Vibe Coding with Streamlit</p>", unsafe_allow_html=True)
st.markdown("---")
st.caption("데이터 출처: 교육부 나이스(NEIS) API")
