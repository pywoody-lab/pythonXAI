#引入模組
import streamlit as st
import openai as ai

#設定API金鑰
ai.api_key=st.secrets["OPENAI_API_KEY"]

#初始話變數及列表

#初始話對話紀錄
if 'history' not in st.session_state:
    #建立空列表
    st.session_state.history = []

#初始話系統訊息
if'system_message' not in st.session_state:
    #預設系統訊息
    st.session_state.system_message = ('請用繁體中文進行後續對話')

#初始話AI模型
if 'model' not in st.session_state:
    #預設AI模型
    st.session_state.model = 'gpt-4o-mini'

#設定標題
st.title('歡迎使用PYTHON AI')

#設定欄位[4.2.1]
col1,col2,col3=st.columns([4,2,1])
with col1:
    #第一列顯示更新系統訊息
    st.session_state.system_message = st.text_input('系統訊息',st.session_state.system_message)

with col2:
    #第二列顯示AI模型
    st.session_state.model=st.selectbox('AI模型',['gpt-4o-mini','gpt-4o','gpt-4o-search-preview'])

with col3:
    #第三列放垃圾桶
    #空行對齊
    st.markdown('')
    #垃圾桶按鈕
    if st.button('清除記錄'):
        #清空對話紀錄
        st.session_state.history = []
        #重新整理
        st.rerun()

# 從對話紀錄中迭代每個訊息並顯示
    # 如果訊息的角色是使用者
        # 顯示使用者的訊息，使用指定的頭像
    # 否則
        # # 顯示AI助手的訊息，使用指定的頭像

# 顯示對話輸入框，等待使用者輸入訊息

# 如果使用者輸入了訊息
    # 將使用者的訊息加入對話紀錄
    # 使用openai.chat.completions.create
    # 取得AI助手回傳的訊息內容
    # 將AI助手的訊息加入對話紀錄
    # 重新整理頁面以顯示新的訊息

for message in st.session_state.history:
    if message["role"] == "user":#角色==使用者
        st.chat_message("user",avatar='😀').write(message["content"])#顯示訊息+頭像
    else: 
        st.chat_message("assistant",avatar='📞').write(message["content"]) #顯示訊息+頭像

prompt=st.chat_input("請輸入問題")#顯示輸入框並等待使用者輸入

if prompt:
    #如果有輸入訊息
    #將使用者的訊息加入對話紀錄
    st.session_state.history.append({"role":"user","content":prompt})
    response=ai.chat.completions.create(
        model=st.session_state.model,
        messages=[{'role':'system','content':st.session_state.system_message}]+st.session_state.history,)
    
    assistant_message=response.choices[0].message.content#取得回答內容
    st.session_state.history.append({"role":"assistant","content":assistant_message})
    #將AI助手的訊息加入對話紀錄
    st.rerun()#重新整理頁面以顯示新的訊息






