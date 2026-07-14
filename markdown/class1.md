# Python 入門筆記

## 1. 第一個 Python 程式：`print()`

`print()` 是用來**把文字或資料顯示在畫面上**的指令。

```python
print("Hello World!")
print("吳定元")
print("woody-wu")
```

執行後會依序顯示：

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
st.markdown("""
# 大標題

## 第二層標題

- 第一項
- 第二項

**粗體**

*斜體*
""")
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
