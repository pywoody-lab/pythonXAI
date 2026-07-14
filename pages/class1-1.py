print('Hello world!')
print('吳定元')
print('woody-wu')
print('不要低頭\n雙下巴會出來')
'''
這是多行註解
'''
#這是單行註解
print('Hello world!')#print是在終端機顯示文字的指令
#ctrl+?能快速註解或取消註解
#基本型態
print(1)#int是整數,-1,0,1,2
print(1.0)#float是浮點數
print(1.234)#float是浮點數
print('apple')#str是字串"sadasd123125557","1"
print(True)#bool是布林值,True/False
print(False)#bool是布林值,True/False
#變數
a=10#新增一個新的儲存空間並取名為a,並用'='將左邊的10放入右邊的a中
print(a)#在終端機顯示a存的值
a='apple'#將a的直改為'apple'
print(a)#在終端機顯示a存的值
#運算子
print(1+1)#加法
print(1-1)#減法
print(1*1)#乘法
print(1/1)#除法
print(1//1)#取商
print(1%1)#取餘數
print(2**3)#次方
# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
#字串運算，+,*
print('apple '+'pen')#字串加法
print('apple '*3)#字串乘法
# 字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
#type()可以查看變數的型態
print(type(1))#<class 'int'>
print(type(1.0))#<class 'float'>
print(type('apple'))#<class 'str'>
print(type(True))#<class 'bool'>
#型態轉換
print(int(1.0))#將浮點數轉為整數
print(float(1))#將整數轉為浮點數
print(str(1))#將整數轉為字串
print(bool(1))#將整數轉為布林值
print(int(1.234))#將浮點數轉為整數
print(float('1.234'))#將字串轉為浮點數
print(str(1.234))#將浮點數轉為字串
print(bool(1.234))#將整數轉為布林值
#print(int('hello'))#將字串轉為整數,會報錯
#請玩家輸入圓的半徑，計算圓面積
r=int(input('請輸入圓的半徑:'))
print(f"圓的面積是: {3.14 * r ** 2}")
#平均計算
a=int(input('請輸入國語期中成績:'))
b=int(input('請輸入國語期末成績:'))
print(f"平均成績是: {(a + b) / 2}")