import streamlit as st
num=st.number_input('請輸入1-9的整數', step=1, min_value=1, max_value=9)
st.write('數字塔:')
for i in range(1,num+1,1):
    st.write(f'{i}'*i)