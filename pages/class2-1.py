#比較運算子，只能同類型比較
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 5)  # True
print(5 <= 5)  # True
print(5 == 5)  # True
print(5 != 3)  # True
#邏輯運算子
#and只要單一條件為false，整個條件就為false
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
#or只要單一條件為true，整個條件就為true
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False
# not 運算子
print(not True)  # False
print(not False)  # True
# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
a=int(input("請輸入密碼:"))
if a == 292081:
    print("吳定元密碼正確")
elif a == 110037:
    print("陳品希密碼正確")
else:
    print("密碼錯誤")
#連續使用if,elif,else和只使用if的差別
#elif能排除前面判斷過的條件，減少複雜度與時間
#用多個if獨立判斷，每個都要執行，效率最低