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