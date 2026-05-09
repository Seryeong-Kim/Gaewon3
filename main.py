import streamlit as st
import requests
from datetime import datetime

# 페이지 설정 및 미니멀 스타일링
st.set_page_config(page_title="개원중 급식", page_icon="🍱", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stTitle { font-weight: 800; color: #333; }
    .meal-card { padding: 20px; border-radius: 15px; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 학교 정보 설정 (서울특별시교육청 - 개원중학교)
ATPT_OFCDC_SC_CODE = "B10" # 서울특별시교육청
SD_SCHUL_CODE = "7010561"   # 개원중학교 코드

def get_meal_info():
    today = datetime.now().strftime("%Y%m%d")
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": today
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data['mealServiceDietInfo'][1]['row'][0]
    except:
        return None

# UI 렌더링
st.title("🍱 개원중 급식 바이브")
st.caption(f"오늘 날짜: {datetime.now().strftime('%Y년 %m월 %d일')}")

meal_data = get_meal_info()

if meal_data:
    meal_list = meal_data['DDISH_NM'].replace("<br/>", "\n")
    calories = meal_data['CAL_INFO']
    
    st.markdown(f"""
    <div class="meal-card">
        <h3>🍴 오늘의 메뉴</h3>
        <p style="white-space: pre-wrap; font-size: 1.1rem; line-height: 1.8;">{meal_list}</p>
        <hr>
        <h4 style="color: #FF4B4B;">🔥 에너지: {calories}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # 칼로리 가이드 (중학생 권장 섭취량 기준 약 800-900kcal)
    cal_value = float(calories.replace(" Kcal", ""))
    if cal_value > 900:
        st.warning(f"⚠️ 오늘은 평소보다 든든하네요! ({cal_value} Kcal)")
    else:
        st.success(f"✅ 적정 칼로리의 식단입니다. ({cal_value} Kcal)")
else:
    st.info("오늘의 급식 정보가 없거나 불러올 수 없습니다. (주말 또는 공휴일일 수 있어요!)")

st.markdown("---")
st.caption("Developed with Vibe Coding • Data by NEIS")
