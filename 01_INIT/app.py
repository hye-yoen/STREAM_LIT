import streamlit as st
from datetime import datetime,date
import pandas as pd
import numpy as np

#페이지 설정
st.set_page_config(
    page_title="스트림릿 UI 가이드",                 #브라우저 탭 제목
    page_icon="🎉",                                 # 브라우저 탭 아이콘 (이모지 또는 이미지 경로)
    layout="wide",                                  #페이지 레이아웃('centered' | 'wide')
    initial_sidebar_state="collapsed",              # 사이드바 초기 상태 ('auto' | 'expanded' | 'collapsed')
    menu_items={                                    # 우측 상단 메뉴 커스터마이징
        'Get Help' : 'https://docs.streamlit.io/',  # "Get help" 메뉴 링크
        'Report a bug':'https://github.com/streamlit', # "Report a bug" 메뉴 링크
        'About' : '이앱은 streamlit 가이드용 예시 입니다.'  # "About" 메뉴 내용
    }
)

# --------------------------
# 제목 / 텍스트
# --------------------------

st.title("스트림릿 UI 단계별 가이드")
st.header("1단계: 텍스트 표시")
st.subheader("다양한 텍스트 스타일")

st.write("일반 텍스트를 표시합니다.")
st.markdown("**굵은 글씨**와 *기울임* 그리고 `코드` 형식도 가능합니다.")
st.caption("작은 캡션 텍스트입니다.")
st.code("print('코드 블록 예제')", language="python")

st.divider()

# --------------------------
# 입력 위젯
# --------------------------
col1,col2 = st.columns(2)

with col1 :
    st.subheader('첫번째 컬럼')
    text_input = st.text_input("이름을 입력하세요",placeholder="홍길동")
    text_area = st.text_area("메세지를 입력하세요",placeholder="여기에 입력...")
    number_input = st.number_input("숫자 입력",min_value =0 , max_value=100,value = 50)
    # 이벤트 처리
    # st.write('text_input',text_input)
    if text_input:
        st.success(f"이름 : {text_input}")
    if text_area:
        st.info(f"메세지 : {text_area}")
    if number_input:
        st.error(f"숫자 : {number_input}")        


with col2 : 
    st.subheader('선택 위젯')
    selectbox = st.selectbox("옵션 선택",["옵션1","옵션2","옵션3"])
    multiselect=st.multiselect("여러새 서택 가능",["A","B","C","D"])
    radio = st.radio("하나만 선택",["예","아니오","모름"])
    # 이벤트 처리
    st.write('selectbox',selectbox)
    st.write('multiselect',multiselect)
    st.write('radio',radio)

st.divider()

# --------------------------
# 날짜 입력 위젯
# --------------------------

st.header("3단계 : 날짜 및 시간 입력")
col1 , col2 , col3  =st.columns(3)

with col1 : 
    date_input = st.date_input("날짜 선택",value=date.today())
    st.write(f"date_input : {date_input}")

with col2 : 
    time_input = st.time_input("시간선택")
    st.write(f"time_input : {time_input}")

with col3 : 
    slider=st.slider("슬라이더",0,100,50)
    st.write(f"slider : {slider}")

st.divider()

# --------------------------
# 체크 , 토글 입력 위젯
# --------------------------

col1 ,col2 = st.columns(2)

with col1 : 
    checkbox1 = st.checkbox("동의함", value = True)
    checkbox2 = st.checkbox("뉴스레터 구독")
    checkbox3 = st.checkbox("마케팅 수신 동의")
    st.write(f"checkbox1 : {checkbox1}")
    st.write(f"checkbox12 :  {checkbox2}")
    st.write(f"checkbox3 : {checkbox3}")

with col2 : 
    toggle1 = st.toggle("알림 활성화",value=True)
    toggle2 = st.toggle("다크모드")
    toggle3 = st.toggle("자동저장")
    st.write(f"toggle1 : {toggle1}")
    st.write(f"toggle2 : {toggle2}")
    st.write(f"toggle3 : {toggle3}")

st.divider()

# --------------------------
# 버튼
# --------------------------

st.header("3단계 버튼")
col1 , col2 , col3, col4 = st.columns(4)

with col1 : 
    if st.button("일반 버튼",type="primary"):
        st.success("버튼이 클림됨")

with col2 : 
    if st.button("보조 버튼",type="secondary"):
        st.success("보조 버튼 클릭")
with col3 : 
    if st.download_button("다운로드",data="샘플데이터",file_name="sample.txt"):
        st.success("다운로드 시작")

with col4 :
    #임시 데이터 프레임생성
    df_tmp = pd.DataFrame({
        '이름' : ["김병수","박효신","박정현"],
        '나이' : [40,45,42],
        '주소' : ['서울','부산','대구']
    })
    df_tmp.to_csv('/app/dataSet/학생점수.csv',index=False,encoding="utf-8-sig")

    # csv 다운로드 버튼
    with open('/app/dataSet/학생점수.csv','rb') as f:
        st.download_button(
            label = "CSV 다운로드",
            data =f,
            file_name = "학생점수.csv",
            mime = "text/csv"
        )

st.divider()

# --------------------------
# 테이블
# -------------------------- 

st.header("4단계 : 테이블 생성")
col1 , col2 = st.columns(2)
# 샘플데이터 생성
df_tbl = pd.DataFrame({
    '이름' : ['김철수','이명희','박민수','최지연'],
    '나이'  : [25,30,35,28],
    '점수' : [85,92,78,95],
    '등급' :['B','A','C','A']
})

with col1 : 
    st.subheader("일반테이블")
    st.write(df_tbl)

with col2 : 
    st.subheader("데이터 프레임")
    st.dataframe(
        df_tbl,
        use_container_width=True,
        hide_index=True,
        column_config={
            "나이" : st.column_config.ProgressColumn(
                "나이게이지",
                help="나이츠 최대 50세 기준 표시",
                format="%d세",
                min_value=0,
                max_value=100,
                ),

            }   

        )

st.subheader("편집 가능 테이블")
st.data_editor(df_tbl,num_rows="dynamic")

st.divider()
# --------------------------
# 차트만들기
# -------------------------- 
st.header("차트 만들기")
df_chart = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.write(df_chart)

col1, col2 = st.columns(2)

with col1 :
    st.subheader("라인차트")
    st.line_chart(df_chart)
with col2 :
    st.subheader("영역차트")
    st.area_chart(df_chart)  

col1, col2 = st.columns(2)
with col1 :
    st.subheader("막대차트")
    st.bar_chart(df_chart)

with col2 :
    st.subheader("산점도인차트")
    st.scatter_chart(
        df_chart,
        x='A',  # x축 컬럼 지정
        y='B',  # y 축 컬럼 지정
        size='C',  #점의 크기를 'C' 컬럼 값에 따라 다르게 지정 (선택적)
        color='C'  # 점의 색상을 'C' 컬럼 값에 따라 다르게 지정 (선택적)
    )

st.divider()
# --------------------------
# 알림메시지
# -------------------------- 
st.header("6단계 알림메세지")
col1 , col2 = st.columns(2)

with col1 : 
    st.success("성공")
    st.info("정보")

with col2 :
    st.warning("경고 메세지")
    st.error("오류메세지")

st.divider()
# --------------------------
# 프로그래스바 
# -------------------------- 
st.header("7단계 흐로그헤스 바와 스피너")

value = st.number_input("진행률(%)입력 : ",min_value = 0,max_value=100,step=1)

import time;
progress_bar = st.progress(0)
spinner = st.spinner("진행중 :")
if value>0:
    with spinner:
        for i in range(int(value)):
            progress_bar.progress(i + 1)
            time.sleep(0.05)
        st.success("처리완료")

st.divider()
# --------------------------
# 업로드
# --------------------------
import os
st.header("8단계 : 파일 업로드")

col1 , col2 = st.columns(2)

with col1 : 
    # IN MEMORY 방식으로 파일 업로드(주기억자치 임시 저장)
    st.subheader("IN MEMORY 방식")
    uploaded_file_1 = st.file_uploader("파일을 선택하세요",type=['csv','txt','xlsx'],key="uploader_1",accept_multiple_files=True)
    # if uploaded_file_1 :
    #     st.success(f"파일 업로드 성공 : {uploaded_file_1.name}")
    #     st.success(f"파일크기 : {uploaded_file_1.size} byte")
    
     
    # =====================
    # 다운로드 표 
    # =====================
    # 파일이 하나라도 업로드 되었을 경우
    if uploaded_file_1: 
        # 이제 uploaded_files_1은 리스트이므로 len() 사용 가능
        st.success(f"총 {len(uploaded_file_1)}개의 파일 업로드 성공") 
        
        st.markdown("---")
        # 2. 표의 헤더 생성
        cols = st.columns([3, 2, 2])
        cols[0].markdown("**파일 이름**")
        cols[1].markdown("**파일 크기 (bytes)**")
        cols[2].markdown("**다운로드**")
        st.markdown("---")
        
        # 3. 파일 목록 표시 및 다운로드 버튼 생성
        # uploaded_files_1 리스트를 순회하며 각 파일(f) 처리
        for f in uploaded_file_1: 
            file_name = f.name
            file_size = f.size
            file_data = f.getvalue() # 메모리에서 파일 내용을 바이트로 읽기
            
            # 한 행에 파일 정보와 다운로드 버튼 배치
            col1_row, col2_row, col3_row = st.columns([3, 2, 2])
            col1_row.write(file_name)
            col2_row.write(file_size)

            col3_row.download_button(
                label="다운로드",
                data=file_data,
                file_name=file_name,
                mime=f.type,
                # 각 버튼은 고유한 key를 가져야 합니다.
                key=f"inmemory_download_{file_name}" 
            )
    # 파일 삭제로직 함수
def delete_file(file_name_to_delete):
    SAVE_DIR = "/app/dataSet"
    file_path = os.path.join(SAVE_DIR, file_name_to_delete)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        st.toast(f"파일 삭제 성공: {file_name_to_delete}", icon="✔")

        st.session_state['uploader_key_counter'] += 1 
    else:
        st.error(f"오류: 파일을 찾을 수 없습니다: {file_name_to_delete}", icon="✔")

if 'uploader_key_counter' not in st.session_state:
    st.session_state['uploader_key_counter'] = 0

with col2:
    #FILE SYSTEM 방식으로 파일 업로드(보조기억장치 영구저장)
    st.subheader("FILE SYSTEM 방식")
    SAVE_DIR_PATH = "/app/dataSet"
    os.makedirs(SAVE_DIR_PATH, exist_ok=True) # 폴더 없으면 자동 생성
    uploaded_file_2 = st.file_uploader("파일을 선택하세요", type=['csv', 'txt', 'xlsx'], key="uploader_2")

    if uploaded_file_2 is not None:
        # 파일경로설정
        save_path = os.path.join(SAVE_DIR_PATH, uploaded_file_2.name) # /app/dataSet/filename
        # 파일저장
        with open(save_path, "wb") as f:
            f.write(uploaded_file_2.getbuffer())
        
        st.success(f"파일 업로드 성공 : {uploaded_file_2.name}")
        st.success(f"파일 업로드 크기 : {uploaded_file_2.size} byte")
        st.success(f"파일 저장 경로 : {save_path}")

    # =====================
    # 다운로드 및 삭제 표 (디스크 기반)
    # =====================
    
    saved_files = [f for f in os.listdir(SAVE_DIR_PATH) if os.path.isfile(os.path.join(SAVE_DIR_PATH, f))]
    
    if not saved_files: 
        st.info("현재 저장된 파일이 없습니다.")
    else:
        st.markdown("---")
        
        cols = st.columns([3, 2, 2, 2])
        cols[0].markdown("**파일 이름**")
        cols[1].markdown("**파일 크기 (bytes)**")
        cols[2].markdown("**다운로드**")
        cols[3].markdown("**삭제**") 
        st.markdown("---")

        for f in saved_files: 
            file_path = os.path.join(SAVE_DIR_PATH, f)
            
            if not os.path.exists(file_path):
                continue 

            file_size = os.path.getsize(file_path)

            col1_row, col2_row, col3_row, col4_row = st.columns([3, 2, 2, 2])
            col1_row.write(f)
            col2_row.write(file_size)

            with open(file_path, "rb") as file_data:
                col3_row.download_button(
                    label="다운로드",
                    data=file_data,
                    file_name=f,
                    mime="application/octet-stream",
                    key=f"download_{f}"
                ) 
            
            col4_row.button(
                "삭제",
                key=f"delete_{f}",
                on_click=delete_file, 
                args=(f,), 
            )     

st.divider()   
# =====================
# 다운로드 및 삭제 표 (디스크 기반)
# =====================

st.header("9단계 :레이아웃-탭")
# tab1 , tab2, tab3 = st.tabs(["데이터","차트","설정"])

# with tab1:
#     st.write("데이터 탭 내용")
#     st.dataframe(df_tbl, use_controller_width=True)
# with tab2:
#     st.write("차트 탭 내용")
#     st.line_chart(df_tbl)
# with tab3:
#     st.write("설정 탭 나용")
#     st.checkbox("옵션1")
#     st.checkbox("옵션2")


st.divider()
# =====================
# 세션 확장 영역
# =====================

st.header("10단계 : 확장 가능한 세션")

with st.expander("자세히 보기"):
    st.write("여기에 숨겨진 내용")
    st.image("https://via.placeholder.com/400x200" , caption="샘플 이미지")

with st.expander("추가정보"):
    st.write("확장 가능한 섹션은 많은 정보를 깔끔하게 정리 할 수 있습니다.")

st.divider()


# =====================
# 사이드 바 메뉴 추가
# =====================
st.header("11단계 : 사이드 바 메뉴 추가")
with st.sidebar:
    st.title("사이드 바")
    st.write("사이드바에 위젯을 배치 할 수 있습니다.")

    sidebar_select = st.selectbox(
        "메뉴 선택",
        ["홈","대시보드","설정"]
    )

    sidebar_slider = st.slider("사이드 바 슬라이더",0,100,25)

    if st.button("사이드 바 버튼"):
        st.success("사이드바 버튼 클릭!")

    st.write(f"선택된 메뉴 : {sidebar_select}")

    st.divider()

    
# --------------------------
# 12단계: 컨테이너 (UI 그룹화 , 특정영역만 갱신 )
# --------------------------
st.header("12단계: 컨테이너")

container = st.container()
with container:
    st.write("이것은 컨테이너 안의 내용입니다.")
    st.metric(label="온도", value="25°C", delta="+2°C")
    st.metric(label="습도", value="60%", delta="-5%")
st.divider()


# ============================================
# 13단계: 메트릭 표시
# ============================================
st.header("13단계: 메트릭 카드")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("총 매출", "₩1,234,567", "+12%")
    
with col2:
    st.metric("방문자 수", "8,456", "+23%")
    
with col3:
    st.metric("전환율", "3.2%", "-0.5%")
    
with col4:
    st.metric("평균 체류시간", "4분 32초", "+45초")

st.divider()

# ============================================
# 14단계: 색상 선택
# ============================================
st.header("14단계: 색상 선택기")

col1, col2 = st.columns(2)

with col1:
    color = st.color_picker("배경색 선택", "#00f900")
    st.write(f"선택된 색상: {color}")
    
with col2:
    st.markdown(f"""
    <div 
        style="background-color: {color}; 
        padding: 20px; 
        border-radius: 10px;"
        >
        <h3 style="color: white;">선택된 색상 미리보기</h3>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# ============================================
# 15단계: 세션 상태
# ============================================
import streamlit as st
import json, os, time

st.header("15단계: 세션 상태 관리")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ 증가"):
        st.session_state.counter += 1
        
with col2:
    if st.button("➖ 감소"):
        st.session_state.counter -= 1
        
with col3:
    if st.button("🔄 리셋"):
        st.session_state.counter = 0

st.write(f"현재 카운터 값: **{st.session_state.counter}**")

st.divider()

# ============================================
# 16단계: 폼 만들기
# ============================================
with st.form("myform"):
    st.write("폼 안의 모든 입력은 제출 버튼을 눌러야 처리됩니다.")

    form_name = st.text_input("이름")
    form_email = st.text_input("이메일")
    form_message = st.text_area("메세지")

    submitted = st.form_submit_button("제출")

    if submitted :
        if not form_name:
            st.error("이름을 이벽하세요")

        else : 
            st.success(f"{form_name}님 , 폼이 제출되었습니다.")
            st.write(f"이메일 : {form_email}")
            st.write(f"메세지 : {form_message}")

st.divider()


