import streamlit as st
import requests
from datetime import datetime
import calendar

# 페이지 설정
st.set_page_config(page_title="개원중 급식 캘린더", page_icon="📅")

# 학교 정보 (개원중학교)
ATPT_OFCDC_SC_CODE = "B10"
SD_SCHUL_CODE = "7010561"

def get_monthly_meal(target_date):
    """선택한 달의 모든 급식 데이터를 가져옵니다."""
    ym = target_date.strftime("%Y%m")
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": ym  # 월 단위 조회
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if 'mealServiceDietInfo' in data:
            return data['mealServiceDietInfo'][1]['row']
        return []
    except:
        return []

# --- UI 레이아웃 ---
st.title("🏫 개원중 월간 급식 가이드")

# 날짜 선택기 (기본값: 오늘)
selected_date = st.date_input("조회하고 싶은 날짜를 선택하세요", datetime.now())
target_month = selected_date.strftime("%Y년 %m월")

st.subheader(f"✨ {target_month} 급식 리스트")

meals = get_monthly_meal(selected_date)

if not meals:
    st.info("해당 월의 급식 데이터가 없습니다.")
else:
    # 1. 선택한 날짜의 급식 하이라이트
    selected_ymd = selected_date.strftime("%Y%m%d")
    today_meal = next((m for m in meals if m['MLSV_YMD'] == selected_ymd), None)

    if today_meal:
        with st.expander(f"📌 선택한 날짜({selected_date.strftime('%m/%d')}) 메뉴 보기", expanded=True):
            st.markdown(f"**{today_meal['DDISH_NM'].replace('<br/>', ', ')}**")
            st.error(f"🔥 칼로리: {today_meal['CAL_INFO']}")
    
    st.divider()

    # 2. 이번 달 전체 급식 리스트 (표 형태 또는 리스트)
    for meal in meals:
        date_str = meal['MLSV_YMD']
        formatted_date = f"{date_str[4:6]}월 {date_str[6:8]}일"
        
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.write(f"**{formatted_date}**")
            with col2:
                # 칼로리 정보 정제 (숫자만 추출해서 비교)
                cal_val = float(meal['CAL_INFO'].split(' ')[0])
                cal_color = "🔴" if cal_val > 900 else "🟢"
                
                st.write(f"{meal['DDISH_NM'].replace('<br/>', ' | ')}")
                st.caption(f"{cal_color} {meal['CAL_INFO']}")
            st.divider()

st.markdown("---")
st.caption("개원중학교 급식 바이브 • 데이터: 나이스(NEIS) API")
