import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="Vibe Picker", layout="centered")

# 데이터셋
vibe_db = [
    {"name": "Minimal Classic", "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105", "tag": "정갈함", "tip": "슬랙스와 셔츠."},
    {"name": "Soft Romantic", "img": "https://images.unsplash.com/photo-1529133039941-e856b3629146", "tag": "사랑스러움", "tip": "가디건과 스커트."},
    {"name": "Street Hipster", "img": "https://images.unsplash.com/photo-1509631179647-0177331693ae", "tag": "자유로움", "tip": "비니와 와이드팬츠."},
    {"name": "Quiet Luxury", "img": "https://images.unsplash.com/photo-1485968579580-b6d095142e6e", "tag": "고급스러움", "tip": "뉴트럴 톤의 니트."},
    {"name": "Office Siren", "img": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2", "tag": "지적인 무드", "tip": "안경과 셔츠."}
]

st.title("오늘의 추구미 🎲")

# 랜덤 버튼
if st.button("무드 추출하기"):
    res = random.choice(vibe_db)
    st.session_state.vibe = res

# 결과 출력
if 'vibe' in st.session_state:
    v = st.session_state.vibe
    st.divider()
    
    # 에러 방지를 위해 옵션을 최소화한 이미지 태그
    st.image(v["img"], caption=v["name"], use_column_width=True)
    
    st.subheader(f"Target: {v['name']}")
    st.write(f"🏷️ {v['tag']}")
    st.info(f"💡 Advice: {v['tip']}")
else:
    st.write("버튼을 눌러보세요.")
