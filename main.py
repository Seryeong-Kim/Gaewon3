import streamlit as st

# 1. 페이지 기본 설정 (미니멀 브랜딩)
st.set_page_config(page_title="OOTD Archive", page_icon="👗", layout="centered")

# 2. 감각적인 레이아웃을 위한 Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;1,400&family=Noto+Sans+KR:wght@100;300;400&display=swap');
    
    /* 전체 배경 및 폰트 */
    .main { background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Bodoni Moda', 'Noto Sans KR', serif; font-weight: 400; letter-spacing: -0.5px; }
    p, span, button { font-family: 'Noto Sans KR', sans-serif; font-weight: 300; }

    /* 버튼 스타일링: 미니멀 블랙 & 화이트 */
    .stButton>button {
        border-radius: 0px;
        border: 1px solid #000;
        background-color: transparent;
        color: #000;
        padding: 10px 20px;
        transition: all 0.4s ease;
        width: 100%;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: #000;
        color: #fff;
        border: 1px solid #000;
    }

    /* 이미지 카드 스타일 */
    .stImage {
        border-radius: 0px;
        filter: grayscale(20%);
        transition: filter 0.5s ease;
    }
    .stImage:hover { filter: grayscale(0%); }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 구성: 오늘 나의 '추구미' 테마
themes = {
    "Minimalist": {
        "title": "Minimalist Archive",
        "tag": "#절제의미학 #화이트셔츠 #슬랙스",
        "desc": "군더더기 없는 실루엣. 가장 단순한 것이 가장 파워풀합니다.",
        "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=1000&auto=format&fit=crop",
        "advice": "실버 액세서리 하나만 매치하세요."
    },
    "Romantic": {
        "title": "Soft Romance",
        "tag": "#부드러운니트 #실크스커트 #파스텔",
        "desc": "따뜻하고 우아한 분위기. 당신의 다정함이 옷을 통해 드러납니다.",
        "image": "https://images.unsplash.com/photo-1529133039941-e856b3629146?q=80&w=1000&auto=format&fit=crop",
        "advice": "머리는 자연스러운 웨이브를 추천해요."
    },
    "Street Gorpcore": {
        "title": "Modern Nomad",
        "tag": "#바람막이 #카고팬츠 #시티보이",
        "desc": "활동적이지만 세련된 감각. 도심 속의 자유로움을 만끽하세요.",
        "image": "https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=1000&auto=format&fit=crop",
        "advice": "투박한 스니커즈가 오늘 룩의 마침표입니다."
    },
    "Vintage Y2K": {
        "title": "Electric Vintage",
        "tag": "#크롭티 #와이드진 #레트로",
        "desc": "과감한 컬러와 키치한 감성. 오늘의 주인공은 당신입니다.",
        "image": "https://images.unsplash.com/photo-1581044777550-4cfa60707c33?q=80&w=1000&auto=format&fit=crop",
        "advice": "컬러풀한 헤어핀으로 위트를 더해보세요."
    }
}

# 4. 앱 UI 레이아웃
st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>AESTHETIC VIBE</h1>", unsafe_allow_html=True)

# 사이드바 혹은 상단에 테마 선택
st.write("---")
cols = st.columns(4)
selected = None

# 세션 상태를 이용해 선택 유지
if 'vibe' not in st.session_state:
    st.session_state.vibe = "Minimalist"

for i, (name, content) in enumerate(themes.items()):
    if cols[i].button(name):
        st.session_state.vibe = name

# 5. 선택된 테마 전시 (룩북 스타일)
current = themes[st.session_state.vibe]

display_col_left, display_col_right = st.columns([1.2, 1])

with display_col_left:
    st.image(current["image"], use_container_width=True)

with display_col_right:
    st.markdown(f"<p style='color: #888; font-size: 14px;'>{current['tag']}</p>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='margin-top: -10px;'>{current['title']}</h2>", unsafe_allow_html=True)
    st.write("")
    st.write(current["desc"])
    st.markdown("---")
    st.markdown(f"**💡 Editorial Advice**")
    st.info(current["advice"])

# 6. 푸터
st.markdown("<br><br><p style='text-align: center; color: #eee; font-size: 12px; letter-spacing: 2px;'>CURATED BY VIBE CODING</p>", unsafe_allow_html=True)ing with Streamlit</p>", unsafe_allow_html=True)
st.markdown("---")
st.caption("데이터 출처: 교육부 나이스(NEIS) API")
