import streamlit as st
import datetime

st.title("AWS 배포 실습 과제")
st.subheader("Cloud Computing Assignment")

st.write("아래 입력창에 텍스트를 입력하고 버튼을 눌러 로그 생성을 테스트하세요.")

user_msg = st.text_input("전송할 메시지 입력", placeholder="여기에 내용을 작성하세요")

# 버튼 및 결과 출력
if st.button("데이터 전송"):
    if user_msg:
        st.info(f"입력 확인: {user_msg}")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[User Action] Time: {current_time} | Input: {user_msg}")
    else:
        st.warning("메시지를 입력해주세요.")