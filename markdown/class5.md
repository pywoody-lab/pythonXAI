# Python 課堂筆記（四）

## 主題：圖片元件、購物平台、OpenAI API、聊天介面（Chat）

---

# 一、圖片元件（Image）

在 Streamlit 中，可以利用 `st.image()` 顯示圖片。

基本語法：

```python
st.image("圖片路徑")
```

例如：

```python
st.image("image/apple.png", width=300)
```

代表：

- 顯示 `apple.png`
- 寬度設定為 300 像素（pixel）

---

## width 參數

```python
st.image("image/apple.png", width=300)
```

`width` 可以設定圖片寬度。

例如：

| width | 效果   |
| ----- | ------ |
| 100   | 小圖片 |
| 300   | 中圖片 |
| 500   | 大圖片 |

---

## use_container_width

```python
st.image(
    "image/apple.png",
    use_container_width=True
)
```

代表：

圖片會自動放大或縮小，填滿目前所在的欄位。

通常做購物網站時很常使用。

---

# 二、os 模組

匯入：

```python
import os
```

`os` 是 Python 內建模組，可以操作檔案與資料夾。

---

## os.listdir()

```python
image_files = os.listdir("image")
```

功能：

取得資料夾內所有檔案。

例如：

```text
image/

apple.png
banana.png
orange.png
bg.png
```

得到：

```python
[
"apple.png",
"banana.png",
"orange.png",
"bg.png"
]
```

---

## os.path.join()

```python
img_path = os.path.join(
    "image",
    "apple.png"
)
```

結果：

```text
image/apple.png
```

好處：

不用自己手動加 `/`，不同作業系統都能正確建立路徑。

---

## os.path.exists()

```python
os.path.exists(img_path)
```

功能：

檢查檔案是否存在。

如果存在：

```python
True
```

不存在：

```python
False
```

---

# 三、購物平台

這次利用 Dictionary 建立商品資料。

例如：

```python
inventory = {
    "蘋果":{
        "price":10,
        "stock":10
    }
}
```

每個商品都有：

- 價格（price）
- 圖片（image）
- 庫存（stock）

---

## number_input()

```python
buy_qty = st.number_input(
    "購買數量",
    min_value=0,
    max_value=庫存
)
```

限制：

- 最少 0
- 最多不能超過庫存

避免買超過庫存。

---

## 購買商品

按下按鈕：

```python
st.button("購買")
```

如果數量大於 0：

```python
庫存 = 庫存 - 購買數量
```

例如：

```text
原本：

蘋果：10

買3個

↓

剩下：

7
```

---

## 補貨

輸入：

- 商品名稱
- 補貨數量

例如：

```text
蘋果

5
```

按下：

```text
確認補貨
```

就會變成：

```text
原本：

7

↓

12
```

---

# 四、提示訊息

Streamlit 有很多不同顏色的提示。

## success()

```python
st.success("成功！")
```

綠色成功訊息。

---

## warning()

```python
st.warning("請重新輸入")
```

黃色警告。

---

## error()

```python
st.error("找不到商品")
```

紅色錯誤訊息。

---

# 五、OpenAI API

可以讓 Python 和 AI 對話。

需要先匯入：

```python
import openai
```

以及：

```python
from dotenv import load_dotenv
```

---

## .env

API 金鑰不能直接寫在程式裡。

通常放在：

```text
.env
```

例如：

```text
OPENAI_API_KEY=你的API金鑰
```

程式利用：

```python
load_dotenv()
```

讀取。

再利用：

```python
os.getenv()
```

取得金鑰。

---

# 六、AI 對話流程

使用者：

```text
你好
```

↓

Python

↓

OpenAI

↓

AI 回覆：

```text
你好！
```

↓

印出答案。

---

## 結束聊天

```python
if user_input.lower() in [
    "exit",
    "quit"
]
```

輸入：

```text
exit
```

或

```text
quit
```

即可結束程式。

---

# 七、messages（對話紀錄）

第一次聊天：

```python
messages=[
    {
        "role":"system",
        "content":"..."
    }
]
```

之後：

使用者說話：

```python
messages.append({
    "role":"user",
    "content":訊息
})
```

AI 回答：

```python
messages.append({
    "role":"assistant",
    "content":回答
})
```

這樣 AI 就能記得前面的聊天內容。

---

## role 的意思

共有三種角色：

| role      | 功能           |
| --------- | -------------- |
| system    | 設定 AI 的規則 |
| user      | 使用者說的話   |
| assistant | AI 回答        |

---

# 八、聊天介面（Chat）

Streamlit 可以直接建立聊天畫面。

例如：

```python
st.chat_message("user")
```

會出現：

💬 使用者聊天泡泡。

---

```python
st.chat_message("assistant")
```

會出現：

🤖 AI 聊天泡泡。

---

## avatar

可以更換聊天頭像。

例如：

```python
avatar="🪄"
```

或

```python
avatar="✨"
```

聊天畫面會更生動。

---

# 九、聊天輸入框

```python
prompt = st.chat_input(
    "請輸入訊息"
)
```

畫面下方會出現：

```text
請輸入訊息……
```

使用者輸入後，

文字會存到：

```python
prompt
```

---

# 十、聊天紀錄

第一次開啟：

```python
st.session_state.history=[]
```

建立聊天紀錄。

之後每一句話都加入：

```python
history.append(...)
```

例如：

```text
使用者：

你好
```

↓

```text
AI：

你好！
```

↓

```text
使用者：

今天天氣如何？
```

全部都會保留下來。

---

## 顯示聊天紀錄

利用：

```python
for message in history:
```

依序顯示所有聊天內容。

畫面就會像：

```text
🪄 你好

✨ 哈囉！

🪄 今天星期幾？

✨ 今天是星期五。
```

---

## st.rerun()

當聊天送出後：

```python
st.rerun()
```

重新整理畫面。

新的聊天內容就會立刻出現在聊天視窗。

---

# 本次課程重點整理

✅ `st.image()` 可以顯示圖片，並用 `width` 或 `use_container_width` 控制大小。
✅ `os.listdir()` 可以取得資料夾內所有檔案。
✅ `os.path.join()` 可以安全地組合檔案路徑。
✅ `os.path.exists()` 可以檢查檔案是否存在。
✅ Dictionary 很適合儲存商品資料，例如價格、圖片與庫存。
✅ `st.success()`、`st.warning()`、`st.error()` 可以顯示不同類型的提示訊息。
✅ `.env` 用來安全存放 API 金鑰，避免直接寫在程式中。
✅ `messages` 會保存 AI 與使用者的對話內容，讓 AI 能理解聊天上下文。
✅ `st.chat_message()` 可以建立聊天泡泡，`st.chat_input()` 提供使用者輸入訊息。
✅ `st.session_state` 可以保存聊天紀錄，搭配 `st.rerun()` 更新畫面，完成基本的聊天機器人介面。
