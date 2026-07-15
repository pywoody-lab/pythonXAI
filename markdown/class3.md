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

| 參數          | 功能                         |
| ------------- | ---------------------------- |
| `step=1`      | 一次增加或減少 1（限制整數） |
| `min_value=1` | 最小值                       |
| `max_value=9` | 最大值                       |

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

- 數字
- 文字
- 不同型態的資料

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

| 方法                     | 適合情況                   |
| ------------------------ | -------------------------- |
| `for i in L`             | 只需要讀資料               |
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

| 指令                | 功能                           |
| ------------------- | ------------------------------ |
| `st.number_input()` | 輸入數字                       |
| `st.text_input()`   | 輸入文字                       |
| `st.columns()`      | 建立多欄版面                   |
| `with`              | 在指定欄位中放入多個元件       |
| `st.session_state`  | 儲存資料，不會因重新整理而消失 |
| `st.rerun()`        | 重新執行整個程式               |
| `L.sort()`          | 將 List 排序                   |
| `len(L)`            | 取得 List 的長度               |
| `for i in L`        | 依序讀取 List 中的每個元素     |
| `range()`           | 建立迴圈範圍                   |
