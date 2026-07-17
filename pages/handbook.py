import streamlit as st
st.title('奇點PYTHON課程筆記')
with st.expander("DAY1筆記"):
    st.write(
        """
        # Python 入門筆記

        ## 1. 第一個 Python 程式：`print()`

        `print()` 是用來**把文字或資料顯示在畫面上**的指令。

        ```python
        print("Hello World!")
        print("吳定元")
        print("woody-wu")
        ```

        執行後會依序顯示:

        ```
        Hello World!
        吳定元
        woody-wu
        ```

        ---

        ## 2. 換行符號 `\n`

        `\n` 代表**換到下一行**。

        ```python
        print("不要低頭\n雙下巴會出來")
        ```

        顯示結果：

        ```
        不要低頭
        雙下巴會出來
        ```

        ---

        ## 3. 註解（Comment）

        註解是寫給自己或其他程式設計師看的說明，**電腦不會執行**。

        ### 單行註解

        ```python
        # 這是一行註解
        ```

        ### 多行註解

        ```python
        '''
        這是第一行
        這是第二行
        '''
        ```

        💡 小技巧：

        - **Ctrl + /** 可以快速註解或取消註解。

        ---

        # 4. Python 的基本資料型態

        Python 常見有四種基本資料型態：

        | 型態    | 名稱             | 範例                 |
        | ------- | ---------------- | -------------------- |
        | `int`   | 整數             | `1`、`10`、`-5`      |
        | `float` | 浮點數（有小數） | `3.14`、`1.0`        |
        | `str`   | 字串（文字）     | `"apple"`、`"Hello"` |
        | `bool`  | 布林值（真假）   | `True`、`False`      |

        例如：

        ```python
        print(1)
        print(3.14)
        print("apple")
        print(True)
        print(False)
        ```

        ---

        # 5. 變數（Variable）

        變數就像一個**貼上名字的盒子**，可以把資料放進去。

        ```python
        a = 10
        print(a)
        ```

        輸出：

        ```
        10
        ```

        變數的內容可以改變：

        ```python
        a = "apple"
        print(a)
        ```

        輸出：

        ```
        apple
        ```

        ---

        # 6. 數學運算

        Python 可以直接做數學計算。

        | 運算   | 符號 | 範例            |
        | ------ | ---- | --------------- |
        | 加法   | `+`  | `1 + 2`         |
        | 減法   | `-`  | `5 - 3`         |
        | 乘法   | `*`  | `3 * 4`         |
        | 除法   | `/`  | `10 / 2`        |
        | 取商   | `//` | `10 // 3` → `3` |
        | 取餘數 | `%`  | `10 % 3` → `1`  |
        | 次方   | `**` | `2 ** 3` → `8`  |

        ---

        # 7. 運算優先順序

        Python 的計算順序和數學很像：

        1. `()` 括號
        2. `**` 次方
        3. `*` `/` `//` `%`
        4. `+` `-`

        例如：

        ```python
        print((3 + 2) * 4)
        ```

        會先算括號。

        ---

        # 8. 字串運算

        ## 字串相加

        ```python
        print("apple " + "pen")
        ```

        結果：

        ```
        apple pen
        ```

        ---

        ## 字串重複

        ```python
        print("apple " * 3)
        ```

        結果：

        ```
        apple apple apple
        ```

        ---

        # 9. f-string（字串格式化）

        可以把變數放進文字裡。

        ```python
        name = "Apple"
        age = 18

        print(f"Hello, my name is {name}, I'm {age} years old.")
        ```

        輸出：

        ```
        Hello, my name is Apple, I'm 18 years old.
        ```

        只要把變數放進 `{}` 裡即可。

        ---

        # 10. 查看資料型態：`type()`

        使用 `type()` 可以知道資料是哪一種型態。

        ```python
        print(type(1))
        print(type(3.14))
        print(type("apple"))
        print(type(True))
        ```

        結果：

        ```
        <class 'int'>
        <class 'float'>
        <class 'str'>
        <class 'bool'>
        ```

        ---

        # 11. 型態轉換

        有時候需要把資料轉成其他型態。

        | 指令      | 功能       |
        | --------- | ---------- |
        | `int()`   | 轉成整數   |
        | `float()` | 轉成浮點數 |
        | `str()`   | 轉成字串   |
        | `bool()`  | 轉成布林值 |

        例如：

        ```python
        print(int(3.14))
        print(float(10))
        print(str(123))
        print(bool(1))
        ```

        結果：

        ```
        3
        10.0
        123
        True
        ```

        ⚠️ 注意：

        ```python
        int("hello")
        ```

        這樣會發生錯誤，因為 `"hello"` 不能變成整數。

        ---

        # 12. 使用者輸入：`input()`

        `input()` 可以讓使用者輸入資料。

        例如：

        ```python
        name = input("請輸入姓名：")
        print(name)
        ```

        因為 `input()` 得到的是**字串**，如果要計算，就要轉成整數：

        ```python
        age = int(input("請輸入年齡："))
        ```

        ---

        # 13. 範例：計算圓面積

        公式：

        > 圓面積 = π × 半徑²

        程式：

        ```python
        r = int(input("請輸入圓的半徑："))
        print(f"圓的面積是：{3.14 * r ** 2}")
        ```

        ---

        # 14. 範例：計算平均成績

        ```python
        a = int(input("請輸入國語期中成績："))
        b = int(input("請輸入國語期末成績："))

        print(f"平均成績是：{(a + b) / 2}")
        ```

        ---

        # 15. Streamlit：快速製作網頁

        Streamlit 是 Python 的套件，可以把 Python 程式變成簡單的網頁。

        首先要先匯入：

        ```python
        import streamlit as st
        ```

        其中：

        - `import`：匯入套件。
        - `streamlit`：套件名稱。
        - `as st`：幫它取一個較短的名稱，以後只要寫 `st`。

        ---

        ## (1) 標題

        ```python
        st.title("這是標題")
        ```

        會顯示一個大標題。

        ---

        ## (2) `st.write()`

        可以顯示很多種資料，例如：

        - 文字
        - 數字
        - 表格
        - Markdown

        ```python
        st.write("Hello")
        ```

        ---

        ## (3) `st.text()`

        只能顯示純文字。

        ```python
        st.text("Hello")
        ```

        ---

        ## (4) `st.markdown()`

        可以使用 Markdown 排版。

        例如：

        ```python
        st.markdown(\"""
        # 大標題

        ## 第二層標題

        - 第一項
        - 第二項

        **粗體**

        *斜體*
        \""")
        ```

        可以做出：

        - 標題
        - 清單
        - 粗體
        - 斜體
        - 程式碼
        - 分隔線
        - 超連結

        等漂亮的排版。

        ---

        # Markdown 常用語法

        | 語法       | 功能       |
        | ---------- | ---------- |
        | `#`        | 第一層標題 |
        | `##`       | 第二層標題 |
        | `###`      | 第三層標題 |
        | `-`        | 項目清單   |
        | `**文字**` | 粗體       |
        | `*文字*`   | 斜體       |
        | `---`      | 分隔線     |
        | ```python  | 程式碼區塊 |

        ---

        # 本章重點整理

        ✅ `print()`：顯示資料。

        ✅ `#`：單行註解。

        ✅ `''' '''`：多行註解。

        ✅ 四種基本型態：

        - `int`（整數）
        - `float`（浮點數）
        - `str`（字串）
        - `bool`（布林值）

        ✅ 變數可以儲存資料。

        ✅ 常用運算：

        - `+`
        - `-`
        - `*`
        - `/`
        - `//`
        - `%`
        - `**`

        ✅ `type()`：查看資料型態。

        ✅ `int()`、`float()`、`str()`、`bool()`：型態轉換。

        ✅ `input()`：接收使用者輸入。

        ✅ `f"{變數}"`：把變數放進字串中。

        ✅ `import streamlit as st`：匯入 Streamlit。

        ✅ `st.title()`：標題。

        ✅ `st.write()`：顯示各種資料。

        ✅ `st.text()`：顯示純文字。

        ✅ `st.markdown()`：使用 Markdown 排版。

        ---

        # 一句話總結

        **Python 的基礎就是：會輸出 (`print`)、會存資料（變數）、會計算（運算子）、會接收輸入 (`input`)，再搭配 Streamlit，就能開始製作簡單的互動式網頁。**
        """
    )
with st.expander("DAY2筆記"):
    st.write(
        """
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

        """
    )
with st.expander("DAY3筆記"):

    st.write(
    """
# Python 課堂筆記（二）

## 主題：for 迴圈、串列(List)、Streamlit 版面配置與狀態儲存

---

# 一、數字塔練習

## number_input()

可以讓使用者輸入數字。

```python
num = st.number_input(
    "請輸入1~9的整數",
    step=1,
    min_value=1,
    max_value=9
)
```

### 常用參數

| 參數            | 功能              |
| ------------- | --------------- |
| `step=1`      | 一次增加或減少 1（限制整數） |
| `min_value=1` | 最小值             |
| `max_value=9` | 最大值             |

---

## 利用 for 迴圈畫數字塔

```python
for i in range(1, num+1):
    st.write(f"{i}" * i)
```

### 執行結果（假設輸入 5）

```
1
22
333
4444
55555
```

### 說明

```python
f"{i}"
```

代表把數字轉成文字。

```python
* i
```

代表把文字重複很多次。

例如：

```
"3" * 3
```

結果就是

```
333
```

---

# 二、串列（List）

List 可以一次儲存很多資料。

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

裡面可以放：

* 數字
* 文字
* 不同型態的資料

---

## sort() 排序

```python
L.sort()
```

功能：

把串列依照大小排序。

例如：

```python
L = [5,2,8,1]
```

排序後：

```
[1,2,5,8]
```

> **注意：List 中的資料型態要一致（例如全部都是數字），否則可能無法排序。**

---

# 三、走訪 List（讀取資料）

有兩種常見方法。

---

## 方法一：利用 index（索引）

```python
for i in range(0, len(L), 2):
    print(L[i])
```

### 說明

```
len(L)
```

代表 List 的長度。

```
range(0, len(L), 2)
```

表示：

從第 0 個開始，每次跳 2 個。

例如：

```
L=[1,2,3,"a","b","c"]
```

會印出：

```
1
3
b
```

---

## 方法二：直接讀資料

```python
for i in L:
    print(i)
```

結果：

```
1
2
3
a
b
c
```

### 優點

不用知道資料的位置。

最常使用。

---

## 兩種方法比較

| 方法                       | 適合情況          |
| ------------------------ | ------------- |
| `for i in L`             | 只需要讀資料        |
| `for i in range(len(L))` | 需要知道資料的位置（索引） |

---

# 四、Streamlit 欄位（Columns）

Columns 可以把畫面切成很多欄。

---

## 建立兩欄

```python
col1, col2 = st.columns(2)
```

畫面：

```
| col1 | col2 |
```

---

## 不同寬度

```python
col1, col2 = st.columns([1,2])
```

表示：

```
col1 : col2

 1   :   2
```

第二欄比較寬。

---

## 建立三欄

```python
col1,col2,col3 = st.columns([1,2,3])
```

畫面比例：

```
1 : 2 : 3
```

---

# 五、with 的用法

如果一個欄位裡面要放很多元件，可以使用：

```python
with col1:
```

例如：

```python
with col1:
    st.button("按鈕")
    st.write("文字")
```

代表：

按鈕和文字都放在 col1。

---

# 六、利用 for 建立很多欄位

```python
cols = st.columns(4)
```

建立四個欄位。

再利用：

```python
for i in range(len(cols)):
```

依序放入按鈕。

這樣就不用自己一直重複寫程式。

---

# 七、Columns 排列方式

## 第一種

```python
col1
按鈕1
按鈕2
按鈕3

col2
文字
文字
文字
```

同一欄會一直往下排列。

---

## 第二種

每次迴圈建立新的兩欄：

```
按鈕1    文字1

按鈕2    文字2

按鈕3    文字3
```

畫面會更整齊。

---

# 八、文字輸入（text_input）

```python
text = st.text_input(
    "輸入欄位標題",
    value="預設顯示文字"
)
```

功能：

讓使用者輸入文字。

例如：

```
請輸入姓名：

王小明
```

可以利用：

```python
st.write(text)
```

把輸入內容顯示出來。

---

# 九、session_state（狀態儲存）

## 問題

如果直接寫：

```python
ans = 1
```

每次按按鈕重新整理後，

程式都會重新開始。

所以：

```
1
→按一下
2
→再按一下
又變回2
```

因為程式重新執行時，

```
ans = 1
```

又重新設定了。

---

## session_state

可以把資料永久存在網頁裡。

第一次沒有資料時：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

代表：

第一次建立

```
ans1 = 1
```

以後就不會重新設定。

---

## 按鈕加一

```python
if st.button("按下去"):
    st.session_state.ans1 += 1
```

每按一次：

```
1
2
3
4
5
……
```

都會一直累加。

---

# 十、st.rerun()

```python
st.rerun()
```

功能：

重新執行整個程式。

有些按鈕按下後，

畫面不一定會立刻更新，

這時可以使用：

```python
st.rerun()
```

強制重新整理畫面。

---

# 本次課程重點整理

✅ `number_input()` 可以限制輸入數字的範圍。
✅ `for` 搭配 `range()` 可以重複執行程式，也能製作數字塔。
✅ List（串列）可以一次存放很多資料。
✅ `sort()` 可以將 List 排序（資料型態需一致）。
✅ 讀取 List 有兩種方式：利用索引（index）或直接讀取元素。
✅ `columns()` 可以把 Streamlit 網頁切成多個欄位，讓畫面更整齊。
✅ `with` 可以在同一欄位中放入多個元件。
✅ `text_input()` 可以讓使用者輸入文字。
✅ `session_state` 可以保存資料，不會因為重新整理而重置。
✅ `st.rerun()` 可以強制重新執行程式，更新畫面。

---

# 本次新增指令整理

| 指令                  | 功能               |
| ------------------- | ---------------- |
| `st.number_input()` | 輸入數字             |
| `st.text_input()`   | 輸入文字             |
| `st.columns()`      | 建立多欄版面           |
| `with`              | 在指定欄位中放入多個元件     |
| `st.session_state`  | 儲存資料，不會因重新整理而消失  |
| `st.rerun()`        | 重新執行整個程式         |
| `L.sort()`          | 將 List 排序        |
| `len(L)`            | 取得 List 的長度      |
| `for i in L`        | 依序讀取 List 中的每個元素 |
| `range()`           | 建立迴圈範圍           |


"""
)
with st.expander("DAY4筆記"):
    (
        '''


# Python 課堂筆記（三）

## 主題：while 迴圈、Random、字典(Dictionary)、Streamlit 點餐機

---

# 一、Streamlit 點餐機

這次利用 Streamlit 做了一個簡單的點餐系統。

主要功能有：

* 新增餐點
* 顯示購物車
* 刪除餐點
* 重新整理畫面

---

## 1. 建立購物車

```python
if "cart" not in st.session_state:
    st.session_state.cart = []
```

### 說明

`cart`（購物車）是一個 List。

第一次開啟網頁時：

```
[]
```

代表購物車是空的。

之後新增餐點都會存到這個 List。

---

## 2. 新增餐點

```python
food = st.text_input("請輸入餐點")
```

使用者輸入餐點名稱。

例如：

```
漢堡
```

按下

```
加入購物車
```

後：

```python
st.session_state.cart.append(food)
```

就會把餐點加入 List。

例如：

```
["薯條"]

↓

["薯條","漢堡"]
```

---

## 3. append()

```python
L.append(資料)
```

功能：

把資料放到 List 最後面。

例如：

```python
L=[1,2]
```

加入：

```python
L.append(3)
```

變成：

```
[1,2,3]
```

---

## 4. pop()

```python
L.pop(index)
```

功能：

刪除指定位置的資料。

例如：

```python
L=["薯條","漢堡","可樂"]
```

```python
L.pop(1)
```

結果：

```
["薯條","可樂"]
```

---

## 5. st.rerun()

每次新增或刪除餐點後，

使用：

```python
st.rerun()
```

重新執行程式。

畫面就會立刻更新。

---

# 二、time.sleep()

```python
import time
```

```python
time.sleep(1)
```

代表：

程式暫停 1 秒。

例如：

```
顯示成功訊息

↓

等待1秒

↓

重新整理
```

---

# 三、算數指定運算子

算數指定運算子可以讓程式更簡潔。

| 寫法        | 等於           |
| --------- | ------------ |
| `a += 1`  | `a = a + 1`  |
| `a -= 1`  | `a = a - 1`  |
| `a *= 2`  | `a = a * 2`  |
| `a /= 2`  | `a = a / 2`  |
| `a //= 2` | `a = a // 2` |
| `a %= 2`  | `a = a % 2`  |
| `a **= 2` | `a = a ** 2` |

### 常見用途

增加計數：

```python
count += 1
```

累加總和：

```python
total += score
```

---

# 四、while 迴圈

當不知道要重複幾次時，

通常使用 while。

基本語法：

```python
while 條件:
    程式
```

只要條件成立，

就會一直執行。

例如：

```python
i=0

while i<5:
    print(i)
    i+=1
```

結果：

```
0
1
2
3
4
```

---

## while 的執行流程

```
檢查條件

↓

成立

↓

執行程式

↓

回去再次檢查
```

如果條件變成 False，

就會離開迴圈。

---

# 五、break

```python
break
```

功能：

立即離開目前所在的迴圈。

例如：

```python
for i in range(5):
    if i==3:
        break
```

結果：

```
0
1
2
3
```

遇到 `break` 就停止。

---

### 注意

`break` 只會跳出**目前所在的那一層迴圈**。

如果有巢狀迴圈（迴圈裡還有迴圈），它不會一次跳出所有迴圈。

---

# 六、Random（亂數）

匯入：

```python
import random as rd
```

---

## randrange()

```python
rd.randrange(7)
```

產生：

```
0~6
```

> **和 `range()` 一樣，不包含最後一個數字。**

---

```python
rd.randrange(1,6)
```

產生：

```
1~5
```

---

```python
rd.randrange(1,10,2)
```

可能得到：

```
1
3
5
7
9
```

---

## randint()

```python
rd.randint(1,100)
```

功能：

產生 1～100 的整數。

> **和 `randrange()` 不同，`randint()` 會包含最後一個數字。**

---

# 七、猜數字遊戲

這次利用：

* session_state
* randint()
* if
* rerun()

完成猜數字遊戲。

遊戲流程：

```
電腦先亂數產生答案

↓

玩家輸入數字

↓

太大

↓

更新最大值

↓

太小

↓

更新最小值

↓

猜中

↓

顯示成功並放氣球
```

---

# 八、Dictionary（字典）

Dictionary（字典）是一種儲存資料的方法。

格式：

```python
{
    key : value
}
```

例如：

```python
d={
    "a":1,
    "b":2,
    "c":3
}
```

---

## Key 與 Value

```
"a" → key

1 → value
```

每一組資料都是：

```
key : value
```

---

## Dictionary 特點

✔ 使用 Key 找資料

✔ Key 不可重複

✔ Value 可以重複

✔ 沒有索引（不能用 `d[0]`）

---

# 九、取得資料

例如：

```python
d["a"]
```

得到：

```
1
```

---

# 十、keys()

取得所有 Key。

```python
d.keys()
```

結果：

```
a
b
c
```

---

# 十一、values()

取得所有 Value。

```python
d.values()
```

結果：

```
1
2
3
```

---

# 十二、items()

同時取得 Key 與 Value。

```python
for key,value in d.items():
```

例如：

```
a 1

b 2

c 3
```

---

# 十三、新增與修改

新增：

```python
d["d"]=4
```

修改：

```python
d["a"]=5
```

都是利用 Key。

---

# 十四、pop()

Dictionary 也可以刪除資料。

```python
d.pop("a")
```

代表：

刪除 Key 為

```
"a"
```

的資料。

---

# 十五、in

檢查 Key 是否存在。

```python
"a" in d
```

結果：

```
True
```

> **注意：`in` 檢查的是 Key，不是 Value。**

---

# 十六、巢狀 Dictionary

Dictionary 裡面還可以放 Dictionary。

例如：

```python
grade={
    "小明":{
        "國文":[90,80,70],
        "數學":[85,75,65]
    }
}
```

取得資料：

```python
grade["小明"]["數學"]
```

得到：

```
[85,75,65]
```

再取第一次成績：

```python
grade["小明"]["數學"][0]
```

得到：

```
85
```

---

# 十七、平均成績

利用：

```python
sum()
```

計算總分。

利用：

```python
len()
```

計算有幾筆資料。

平均：

```python
sum(scores)/len(scores)
```

---

# 十八、整理所有成績

可以利用 Dictionary 把每個人的成績整理到一起。

例如：

```
國文：

90
80
70
88
78
68
...
```

之後就可以方便計算：

* 全班平均
* 各科平均
* 最高分
* 最低分

---

# 本次課程重點整理

✅ `append()` 可以把資料加入 List。
✅ `pop()` 可以刪除 List 或 Dictionary 中指定的資料。
✅ `time.sleep()` 可以讓程式暫停指定秒數。
✅ 算數指定運算子（如 `+=`、`-=`）可以簡化程式寫法。
✅ `while` 迴圈會一直執行，直到條件變成 `False`。
✅ `break` 可以立即跳出目前所在的迴圈。
✅ `random.randrange()` 與 `random.randint()` 都能產生亂數，但是否包含最後一個數字不同。
✅ Dictionary（字典）使用 `key : value` 儲存資料，適合建立成績、會員或商品等資料。
✅ 常用字典方法有 `keys()`、`values()`、`items()`、`pop()`。
✅ `session_state` 可以保存遊戲或網頁的資料，例如猜數字答案、購物車內容等，不會因畫面重新整理而消失。

'''
)
with st.expander("DAY5筆記"):
    ('''
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

'''
)