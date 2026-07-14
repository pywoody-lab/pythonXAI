import streamlit as st#匯入streamlit命名為st
#st.number_input使玩家輸入數字，step=1限制輸入整數
#min_value=0設定最小值, max_value=100限制最大值
num=st.number_input('請輸入一個數字', step=1,)
#st.write()函數將輸入的數字顯示在網頁上
st.write(f'你輸入的數字是:{num}')
st.markdown("---")
st.markdown("### 練習")
grade=st.number_input('請輸入一個數字', step=1,min_value=0,max_value=100)
if grade >= 90:
    st.write("成績等第A")  
elif grade >= 80:
    st.write("成績等第B")
elif grade >= 70:
    st.write("成績等第C")
elif grade >= 60:
    st.write("成績等第D")
else:
    st.write("成績等第F")
st.markdown("---")
st.markdown("### 按鈕")
#ST.button()函數創建一個按鈕，當按鈕被點擊時，返回True，否則返回False
#Key參數用於指定按鈕的唯一標識符，避免多個按鈕之間的衝突
if st.button('測試',key='button'):
    st.write('已觸發按鈕')
if st.button('驚喜',key='balloons'):
    st.balloons()
if st.button('驚喜',key='snow'):
    st.snow()
if st.button('驚喜',key='toast'):
    st.toast('來吃吐司吧!')
st.markdown("---")