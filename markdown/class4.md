# Python 課堂筆記（三）

## 主題：while 迴圈、Random、字典(Dictionary)、Streamlit 點餐機

---

# 一、Streamlit 點餐機

這次利用 Streamlit 做了一個簡單的點餐系統。

主要功能有：

- 新增餐點
- 顯示購物車
- 刪除餐點
- 重新整理畫面

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

| 寫法      | 等於         |
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

- session_state
- randint()
- if
- rerun()

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

- 全班平均
- 各科平均
- 最高分
- 最低分

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
