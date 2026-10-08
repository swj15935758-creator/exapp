# exapp.py
# 주제 우선순위 계산기

import os
import streamlit as st
from dotenv import load_dotenv


# 할 일 입력: st.text_input()으로 해야 할 일을 입력
# 중요도 선택: st.slider()로 1~5
# 긴급도 선택: st.slider()로 1~5
# 예상 소요시간 입력: st.number_input()으로 몇 시간 걸리는지 입력
# 마감일 선택: st.date_input()으로 마감 날짜 선택
# 우선순위 점수 계산: 중요도와 긴급도가 높을수록 점수를 높게 계산
# 등급 출력: 예를 들어 높음 / 보통 / 낮음
# 결과 메시지 출력: st.success(), st.warning(), st.info() 사용
# 진행률 표시: st.progress()로 우선순위 점수 시각화
# 입력값 초기화: st.form(clear_on_submit=True) 사용
# 환경변수 2개 사용: 앱 제목, 높은 우선순위 기준점수 같은 값


def main():
    load_dotenv()

    app_title = os.getenv('APP_TITLE', '우선순위 계산기')
    high_priority_score = int(os.getenv('HIGH_PRIORITY_SCORE', 80))

    st.set_page_config(
        page_title="exapp",
        page_icon='🎯',
        layout="wide",
    )

    st.title(app_title)

    with st.form(
        'priority_form',
        clear_on_submit=True
    ):
        task = st.text_input(
            '할 일📜',
            placeholder='예) Streamlit 과제 제출'
        )

        importance = st.slider(
            '중요도✨',
            min_value=1,
            max_value=5,
            value=3
        )

        urgency = st.slider(
            '긴급도🚑',
            min_value=1,
            max_value=5,
            value=3
        )

        expected_hours = st.number_input(
            '예상 소요시간(기준 1시간)⏰',
            min_value=0.5,
            step=0.5
        )

        deadline = st.date_input(
            '마감일💀'
        )

        submitted = st.form_submit_button(
            '우선순위 계산'
        )

    if not submitted:
        return

    if not task.strip():
        st.warning('할 일을 입력하세요.')
        return

    priority_score = (
        importance * 10
        + urgency * 10
    )

    st.subheader('계산 결과')

    st.write(f'할 일: {task}')
    st.write(f'예상 소요시간: {expected_hours}시간')
    st.write(f'마감일: {deadline}')

    st.metric(
        '우선순위 점수',
        priority_score
    )

    st.progress(priority_score)

    if priority_score >= high_priority_score:
        st.success('우선순위가 높습니다. 먼저 처리하는 것이 좋습니다.')

    elif priority_score >= 50:
        st.warning('우선순위가 보통입니다.')

    else:
        st.info('우선순위가 낮습니다.')


if __name__ == '__main__':
    main()