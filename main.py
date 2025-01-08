import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('\n\n'

st.title('안녕하세요 저는 😘입니다')
st.write('저의 이메일 주소:24_10109@daejin.sen.hs.kr)

import streamlit as st

st.button("Reset", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("Goodbye")

import streamlit as st
import random

# Set the title of the app
st.title("나의 첫번째 앱")

# Add a description
st.write("이 앱은 버튼을 클릭할 때마다 랜덤 숫자를 생성합니다.")

# Create a button that generates a random number when clicked
if st.button("랜덤 숫자 생성"):
    random_number = random.randint(1, 100)
    st.write(f"생성된 랜덤 숫자: {random_number}")
else:
    st.write("버튼을 클릭해 랜덤 숫자를 생성하세요.")
