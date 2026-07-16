import random as rd
import streamlit as st

# 初始化變數
if "ans" not in st.session_state:  
    st.session_state.ans = rd.randint(1, 100) 
if "sm" not in st.session_state:  
    st.session_state.sm = 1 
if "bi" not in st.session_state:  
    st.session_state.bi = 100 
# 新增一個變數來儲存每一次的提示訊息，避免訊息因為重新整理而消失
if "message" not in st.session_state:
    st.session_state.message = ""

st.title("猜數字遊戲")

# 這裡的提示文字會因為 st.rerun() 而即時更新邊界
st.session_state.gus = st.number_input(f"猜一個 {st.session_state.sm} 到 {st.session_state.bi} 之間的整數", value=0)

if st.button("猜!"):
    if st.session_state.gus == st.session_state.ans:
        st.session_state.message = "你猜對了！"
        st.balloons()
    elif st.session_state.gus > st.session_state.ans:
        st.session_state.message = f"{st.session_state.gus} 太大了！"
        st.session_state.bi = st.session_state.gus
        st.rerun()  # 移除了內部的 st.write，直接重跑網頁
    else: 
        st.session_state.message = f"{st.session_state.gus} 太小了！"
        st.session_state.sm = st.session_state.gus
        st.rerun()  # 移除了內部的 st.write，直接重跑網頁

#【移到最外層的最下方】這樣不管網頁怎麼重新整理，訊息都能完美顯示！
if st.session_state.message:
    st.write(st.session_state.message)






