import streamlit as st
import requests
from datetime import datetime

# 1. 페이지 설정 (심플 & 미니멀)
st.set_page_config(page_title="개원중 급식 체크", page_icon="🍚")

# 2. 학교 정보 정의
ATPT_OFCDC_SC_CODE = "B10" # 서울특별시교육청
SD_SCHUL_CODE = "7010561"   # 개원중학교

def get_meal_data(ym):
    """나이스 API에서 해당 월의 급식 데이터를 가져옵니다."""
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": ym
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        # 데이터가 정상적으로 존재할 경우에만 반환
        if 'mealServiceDietInfo' in data:
            return data['mealServiceDietInfo'][1]['row']
        return []
    except:
        return []

# 3. UI 구성
st.title("🍚 개원중학교 급식 리스트")

# 사이드바에서 월 선택 (기본값 현재 월)
now = datetime.now()
selected_month = st.sidebar.selectbox(
    "조회할 월을 선택하세요", 
    [f"{i:02d}" for i in range(1, 13)], 
    index=now.month - 1
)
target_ym = f"{now.year}{selected_month}"

st.subheader(f"📅 {now.year}년 {selected_month}월 식단")

meals = get_meal_data(target_ym)

if not meals:
    st.warning("데이터를 불러올 수 없습니다. (데이터 미등록 또는 API 오류)")
else:
    for meal in meals:
        # 날짜 포맷팅 (20240501 -> 05월 01일)
        date_raw = meal['MLSV_YMD']
        formatted_date = f"{date_raw[4:6]}월 {date_raw[6:8]}일"
        
        # 메뉴 정제 (알레르기 정보 숫자 제거 및 줄바꿈 처리)
        menu = meal['DDISH_NM'].replace("<br/>", "\n")
        import re
        menu = re.sub(r'\([0-9.]+\)', '', menu) # 숫자/마침표 괄호 제거 (깔끔하게)
        
        # 칼로리 정보
        cal_info = meal['CAL_INFO']
        cal_value = float(re.findall(r'\d+\.?\d*', cal_info)[0]) # 숫자만 추출
        
        # 디자인 및 칼로리 경고 (900kcal 기준)
        with st.expander(f"📍 {formatted_date} 식단 보기", expanded=(date_raw == now.strftime("%Y%m%d"))):
            st.text(menu)
            
            if cal_value > 900:
                st.error(f"⚠️ 칼로리 주의: {cal_info} (900kcal 초과!)")
            else:
                st.success(f"✅ 칼로리 적정: {cal_info}")

st.markdown("---")
st.caption("데이터 출처: 교육부 나이스(NEIS) API")
