import streamlit as st 
import time
# 重新整理
if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(1)  # 縮短為1秒加快體驗
    st.rerun()  # 重新整理整個頁面
# 儲存串列
if "cart" not in st.session_state: 
    st.session_state.cart = []  
# 標題
st.title('點餐機')
# 詢問+加入
for i in range(1):
    col1, col2 = st.columns([3,1])
    with col1:
       food = st.text_input('請輸入餐點', value='薯條') # 建議預設值改為具體餐點
    with col2:
         if st.button('加入購物車', key='add'):
            if food: # 確保有輸入內容
                st.session_state.cart.append(food) 
                st.rerun() # 立即更新畫面顯示新餐點
# 副標題
st.markdown("## 購物車")
# 顯示餐點與刪除按鈕
if st.session_state.cart:
    # 為了在迴圈中安全刪除元素，我們需要記錄要刪除的索引
    delete_index = None    
    for i in range(len(st.session_state.cart)):
        # 建立與上方輸入框相同比例的欄位 [3, 1]
        display_col1, display_col2 = st.columns([3, 1])        
        with display_col1:
            st.write(f"▪ {st.session_state.cart[i]}")            
        with display_col2:
            # 使用唯一的 key (例如 del_0, del_1...)，並設定小巧的按鈕樣式
            if st.button("刪除", key=f"del_{i}"):
                delete_index = i # 記錄要刪除的位置                
    # 如果觸發了刪除，將物品從清單移除並重新整理網頁
    if delete_index is not None:
        st.session_state.cart.pop(delete_index)
        st.rerun()
else:
    st.write("購物車是空的")
