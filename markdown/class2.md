# Python 課堂筆記（比較運算、判斷式、迴圈、Streamlit）

## 一、比較運算子（Comparison Operators）

比較運算子用來比較兩個資料是否符合條件，結果只會有兩種：

- `True`：成立（真）
- `False`：不成立（假）

> **注意：通常比較時要使用相同型態的資料，例如數字跟數字比較。**

| 運算子 | 意思     | 範例     | 結果    |
| ------ | -------- | -------- | ------- |
| `>`    | 大於     | `5 > 3`  | `True`  |
| `<`    | 小於     | `5 < 3`  | `False` |
| `>=`   | 大於等於 | `5 >= 5` | `True`  |
| `<=`   | 小於等於 | `5 <= 5` | `True`  |
| `==`   | 等於     | `5 == 5` | `True`  |
| `!=`   | 不等於   | `5 != 3` | `True`  |

---

# 二、邏輯運算子（Logical Operators）

當需要同時判斷很多條件時，就會使用邏輯運算子。

## 1. and（而且）

只有**所有條件都成立**，結果才會是 `True`。

例如：

```python
True and True     # True
True and False    # False
```

### 記憶方法：

只要有一個條件是 False，整個結果就是 False。

---

## 2. or（或者）

只要**其中一個條件成立**，結果就是 `True`。

例如：

```python
True or False     # True
False or True     # True
False or False    # False
```

### 記憶方法：

只要有一個 True，就會得到 True。

---

## 3. not（相反）

`not` 會把布林值反過來。

```python
not True      # False
not False     # True
```

---

# 三、運算子的優先順序

Python 會依照固定順序進行運算。

由高到低：

1. `()` 括號
2. `**` 次方
3. `*`、`/`、`//`、`%`
4. `+`、`-`
5. `==`、`!=`、`>`、`<`、`>=`、`<=`
6. `not`
7. `and`
8. `or`

### 小提醒

如果不確定誰先算，可以加上括號 `()`，讓程式更容易閱讀。

---

# 四、if 判斷式

當程式需要依照不同情況做不同事情時，就會使用 `if`。

基本語法：

```python
if 條件:
    程式

elif 條件:
    程式

else:
    程式
```

例如：

```python
a = int(input("請輸入密碼："))

if a == 292081:
    print("密碼正確")

elif a == 110037:
    print("密碼正確")

else:
    print("密碼錯誤")
```

### 執行流程

1. 先判斷 `if`
2. 如果不符合，再判斷 `elif`
3. 都不符合，就執行 `else`

---

# 五、if 和 elif 的差別

## 使用 if、elif

```python
if ...
elif ...
elif ...
else ...
```

特色：

- 找到符合條件後，就不會再繼續往下判斷。
- 執行速度比較快。
- 程式比較容易閱讀。

---

## 使用很多個 if

```python
if ...
if ...
if ...
```

特色：

- 每個 if 都會執行判斷。
- 即使前面已經符合，後面還是會檢查。
- 執行效率較低。

### 建議

如果只需要選擇其中一個結果，優先使用：

```python
if → elif → else
```

---

# 六、Streamlit 基本功能

Streamlit 可以把 Python 程式變成網頁。

匯入方式：

```python
import streamlit as st
```

---

## 1. number_input()

讓使用者輸入數字。

```python
num = st.number_input(
    "請輸入一個數字",
    step=1
)
```

常用參數：

- `step=1`：一次增加或減少 1（限制輸入整數）
- `min_value=0`：最小值
- `max_value=100`：最大值

---

## 2. st.write()

顯示文字或變數。

```python
st.write("Hello")
st.write(num)
```

也可以使用 f-string：

```python
st.write(f"你輸入的數字是：{num}")
```

---

## 3. st.markdown()

顯示 Markdown 格式文字。

例如：

```python
st.markdown("---")
```

會顯示一條分隔線。

```python
st.markdown("### 練習")
```

會顯示三級標題。

---

## 4. 成績判斷

利用 if 判斷成績等第：

```python
if grade >= 90:
    A
elif grade >= 80:
    B
elif grade >= 70:
    C
elif grade >= 60:
    D
else:
    F
```

---

## 5. 按鈕（button）

建立按鈕：

```python
st.button("按鈕名稱")
```

當按鈕被按下時，會回傳 `True`。

例如：

```python
if st.button("測試"):
    st.write("已觸發按鈕")
```

---

### key 的用途

如果有很多按鈕，要設定不同的 `key`。

例如：

```python
st.button("驚喜", key="balloons")
```

避免按鈕互相衝突。

---

### 特效

彩帶：

```python
st.balloons()
```

下雪：

```python
st.snow()
```

吐司通知：

```python
st.toast("來吃吐司吧！")
```

---

# 七、for 迴圈

for 迴圈可以重複執行相同的程式。

基本語法：

```python
for i in range(5):
    print(i)
```

結果：

```
0
1
2
3
4
```

> **注意：`range(5)` 不包含 5。**

---

## range() 的三種用法

### 1. 只有結束值

```python
range(5)
```

產生：

```
0 1 2 3 4
```

---

### 2. 起始值、結束值

```python
range(1,5)
```

產生：

```
1 2 3 4
```

> 不包含 5。

---

### 3. 起始值、結束值、間隔值

```python
range(1,10,2)
```

產生：

```
1
3
5
7
9
```

每次增加 2。

---

# 八、迴圈變數

```python
for i in range(5):
    print(i)
```

其中：

`i` 稱為**迴圈變數**。

每跑一次迴圈，就會依序取得：

```
0
1
2
3
4
```

---

# 九、在迴圈中存資料

```python
for i in range(5):
    a = i * 2

print(a)
```

執行過程：

```
i=0 → a=0
i=1 → a=2
i=2 → a=4
i=3 → a=6
i=4 → a=8
```

最後印出：

```
8
```

因為每次迴圈都會重新指定 `a` 的值，所以最後留下的是最後一次的結果。

---

# 本次課程重點整理

✅ 比較運算子：比較兩個值，結果只有 `True` 或 `False`。
✅ 邏輯運算子：`and`（全部成立）、`or`（任一成立）、`not`（相反）。
✅ 熟悉運算子的優先順序，必要時使用括號提高可讀性。
✅ `if → elif → else` 可以依照不同條件執行不同程式。
✅ `elif` 比多個 `if` 更有效率，也更容易閱讀。
✅ Streamlit 可以快速製作互動式網頁，例如輸入框、按鈕和動畫。
✅ `for` 迴圈可以重複執行程式，常搭配 `range()` 使用。
✅ `range()` 不包含結束值，可設定起始值與間隔值。
✅ 迴圈中的變數會依序取得每個值，若在迴圈內更新變數，最後會保留最後一次更新的結果。
