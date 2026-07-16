#算數指定運算子
a=1
a+=1#a=a+1
print(a)#2
a-=1#a=a-1
print(a)#1
a*=1#a=a*1
print(a)#2
a/=1#a=a/1
print(a)#1.0
a//=1#a=a//1
print(a)#0
a%=1#a=a%0.1
print(a)#0.0
a**=1#a=a**1
print(a)#0.0
# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算數指定運算子

#while迴圈
#while搭配條件使用
#while Ture 一直執行
#while False 跳出迴圈
#每次執行完會重新檢查是否為False
i=0
while i<5:
    print(i)
    i+=1#i=i+1
#break強制跳出迴圈
#判斷他屬於哪個迴圈並跳出該迴圈
i=0
while i<5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break#跳出while迴圈
    i+=1
for i in range(5):
    print(i)
    if i == 3:
        break#跳出for迴圈
#random模組
import random as rd#匯入random模組
#random.randrange()抽籤範圍跟range相同
print(rd.randrange(7))#1~6
print(rd.randrange(1,6))#1~6
print(rd.randrange(1,6,2))#1~6間隔2
