print([])#這是空的list
print([1,2,3])#這是有三個元素的list
print([1,2,3,'a', 'b', 'c'])#這是有六個元素的list
print([1,2,3,['a', 'b', 'c']])#這是有四個元素的list
print([1,True,'a',1.23])#這是有四個元素的list
#list讀元素，index從零開始
L=[1,2,3,'a','b','c']
print(L[0])#1
print(L[1])#2
print(L[2])#3
print(L[3])#'a'
L=[1,2,3,'a','b','c']
#就是取index0到最後，每次取2格元素，[1,3,'b']
print(L[::2])
#就是取index1到3，不用取4，[2,3,'a']
print(L[1:4])
#就是取index1到3，不用取4，每次取2格元素，[2,'a']
print(L[1:4:2])
#跟range相同用法(符號不同)

#list的append
L=[1,2,3]
L.append(4)#4加在L最後
print(L)
#list移除元素兩種方法
#1.remove移除指定元素
L=['a','b','c','d','a']
L.remove('a')#移除第一個'a'
#remove從前面開始找，刪除第一個
#移除全部符合的元素，應使用迴圈
for i in L:
    if i=='a':
        L.remove(i)

#pop移除指定元素
L=['a','b','c','d','a']
L.pop(0)#移除編號0元素
#pop移除指定元素
#不指定元素則移除最後
L.pop()#移除最後的元素
print(L)
#sort將列表由小到大排序(升序)
#直接改變元列表(不另外建立)
L=[1,3,2,4,5]
L.sort()
print(L)

#list走訪元素
#用index找list資料
#把列表當成讀資料的範圍
#看使用情境決定是否要index(方式)
L=[1,2,3,'a','b','c']
for i in range(0,len(L),2):
    print(L[i])
for i in L:
    print(i)

