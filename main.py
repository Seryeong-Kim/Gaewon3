import streamlit as st
import requests
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="개원중 급식 마스터", page_icon="🏫", layout="wide")

# 2. 스타일링 (미니멀 & 가독성)
st.markdown("""
    <style>
    .meal-card {
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        background-color: #ffffff;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .safe { border-left-color: #28a745; }
    .danger { border-left-color: #dc3545; }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 로직 (나이스 API 활용)
ATPT_OFCDC_SC_CODE = "B10"  # 서울특별시
SD_SCHUL_CODE = "7010561"    # 개원중학교

def fetch_meals(ym):
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": ym
    }
    try:
        res = requests.get(url, params=params)
        data = res.json()
        return data['mealServiceDietInfo'][1]['row']
    except:
        return []

# 4. 사이드바 - 월 선택
st.sidebar.header("📅 조회 설정")
current_year = datetime.now().year
selected_month = st.sidebar.slider("월 선택", 1, 12, datetime.now().month)
target_ym = f"{current_year}{selected_month:02d}"

# 5. 메인 화면 구성
st.title(f"🏫 개원중학교 {selected_month}월 급식 식단표")
st.info("💡 **900kcal**가 넘는 식단은 빨간색으로 표시됩니다.")

meals = fetch_meals(target_ym)

if not meals:
    st.warning("이 달의 급식 데이터가 아직 등록되지 않았습니다.")
else:
    # 데이터를 3열 레이아웃으로 배치
    cols = st.columns(3)
    
    for idx, meal in enumerate(meals):
        with cols[idx % 3]:
            # 데이터 가공
            date_str = datetime.strptime(meal['MLSV_YMD'], "%Y%m%d").strftime("%m/%d (%a)")
            dish_name = meal['DDISH_NM'].replace("<br/>", "\n")
            cal_str = meal['CAL_INFO']
            cal_val = float(cal_str.split(" ")[0])
            
            # 칼로리 기준 판단
            status_class = "danger" if cal_val > 900 else "safe"
            status_icon = "⚠️" if cal_val > 900 else "✅"

            # 카드 출력
            st.markdown(f"""
                <div class="meal-card {status_class}">
                    <h4 style="margin-top:0;">📅 {date_str}</h4>
                    <p style="font-size: 0.95rem; line-height: 1.6; min-height: 150px; white-space: pre-wrap;">{dish_name}</p>
                    <hr>
                    <p style="font-weight: bold; margin-bottom:0;">{status_icon} {cal_str}</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.caption("본 앱은 교육청 공공데이터를 기반으로 실시간 제공됩니다.")
