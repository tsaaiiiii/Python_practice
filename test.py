print('hello world')

age = 20

age = float(age)
print(age)

#  -------------- 2 input 取得使用者輸入 -----------------
# name = input('請輸入名字：')
# print(f"你的名字是 {name}")

# 練習一：填詞
# adj_1 = input('請輸入一個形容詞：')
# adj_2 = input('請輸入一個形容詞：')
# adj_3 = input('請輸入一個形容詞：')
# noun_1 = input('請輸入名詞：')
# verb_1 = input('請輸入動詞：')

# print(f"今天我去了一個{adj_1} 的公園，我看到了一個{adj_2} 的 {noun_1}，他正在{verb_1}，今天是 {adj_3} 的一天")

# 練習二：矩形的面積
# length = input('請輸入長度：')
# width = input('請輸入寬度：')

# area = float(length)*float(width)
# print(f"矩形的面積是 {area}")


# 練習三：購物車程式
# product  = input('物品')
# price = float(input('價格'))
# quantity = int(input('數量'))

# total = price*quantity
# print(f"你購買了 {quantity} 個 {product}，總共花費 {total} 元")


# -------------- 3 數學方法 -----------------
a = 1
a +=1
print(a) # 2

a+=1
print(a) # 3

# 指數（平方、三次方）
b = 2
# b == b**3 // 與下方相同
b **=3

print(b) # 8

# 模數 mod
# 10 mod 3 = 3...1
# 11 mod 3 = 3...2
# 12 mod 3 = 4...0

print(10%3) # 1

# 次方
print(pow(2,10)) # 1024

# 最大最小值
print(max(1,5,2)) # 5
print(min(-3,10,-10)) # -10

# 絕對值
print(abs(-10)) # 10
print(abs(2)) # 2

# 四捨五入
print(round(3.54159)) # 4
print(round(3.1415926)) # 3

# 無條件進位與捨去
import math # 數學模塊的方法要引入
print(math.ceil(3.1)) # 4 無條件進位
print(math.floor(3.9)) # 3 無條件捨去

# 圓周率
print(math.pi) # 3.141592653589793

# 圓周長
r = 10
circumference =2*r*math.pi
print(f"圓周長是 {circumference}")

# 隨機數
import random 
print(random.randint(1,10)) # 1~10 隨機整數


# python 計算機程式
# operation = input('請輸入運算符號（+、-、*、/）：')
# num1 = float(input('請輸入第一個數字：'))
# num2 = float(input('請輸入第二個數字：'))

# if(operation == '+'):
#     result = num1 + num2

# elif(operation == '-'):
#     result = num1-num2

# elif(operation == "*"):
#     result = num1*num2

# elif(operation == '/'):
#     result = num1/num2

# else:
#     print(f"無效")

# print(f"運算結果是: {result}")


## and or not 
tmp = int(input("請輸入現在溫度："))
# if tmp >0 and tmp<30:
#     print(f"溫度不錯")
# else: 
#     print(f"溫度不適宜")


# if tmp >0 or tmp<30:
#     print(f"溫度不錯")
# else: 
#     print(f"溫度不適宜")



# str 方法  

name = 'code hello WORld!!!'

# 幾個字元
length = len(name)
print(f"你的全名共有", length, "個字元")

# 找到第一個空格
space_pos = name.find(" ")
print(f"第一個空格出現在", space_pos,"個字元")

# capitalize() 第一個字母變大寫
name_capitalize = name.capitalize()
print(f"第一個字母變大寫：", name_capitalize)

# upper() 所有變大寫
name_upper = name.upper()
print(f"名字變大寫", name_upper)

# lower() 所有變小寫
name_lower = name.lower()
print(f"所有變小寫", name_lower)


# count 找到你想指定找到的數量
phone_number = input("輸入電話號碼")
dash_count = phone_number.count("-")
print(f"你的電話號碼中有",dash_count,"個短橫線")

# replace 替換
# 將橫線轉換成空格
phone_number = phone_number.replace("-"," ")
print(f"電話號碼，將橫線轉換成空格",phone_number)

# 程式練習：驗證使用者輸入的合法性
# - 使用者名稱不能超過 12 個字元
# - 名稱不能包含空白 (" " in user_name)
# - 名稱不能包含數字 user_name.isalpha() // 都是英文則是 true
# - 都符合：顯示 歡迎 + 使用者名稱

user_name = input("請輸入名稱")

name_length = len(user_name)
if(name_length <= 12 and (user_name.count(" ")==0) and user_name.isalpha()):
    print(f"歡迎",user_name)
else:
    print("名稱輸入錯誤")


# codeshiba 解答
username = input("請輸入你的使用者名稱")

if len(username) > 12:
    print("名稱不能超過 12 個字元")
elif " " in username:
    print("名稱裡不能有空白")
elif not username.isalpha():
    print("名稱不能包含數字")
else:
    print(f"歡迎 " + username)


## email 字串分析
email = 'test@mail.com'
index = email.index('@') # 找到 @ 的位置
print(f"@ 在第",index,"的位置")
print(email[0:index]) #test
print(email[:index]) #縮寫：email[:index]
print(email[index+1:]) # mail.com


# f-string 字串格式化
print_1 = 3.321
print_2 = -77
print_3 = 15.11

# print(f"價格 1 為 {print_1:.2f} \n"

# f"價格 2 為 {print_2:.2f} \n"
# f"價格 3 為 {print_3:.2f}")


# 加上加號

print(f"價格 1 為 {print_1:+.2f} \n"

f"價格 2 為 {print_2:+.2f} \n"
f"價格 3 為 {print_3:+.2f}")

# 字串對齊 < > ^

print(f"價格 1 為 {print_1:<10.2f} \n" # 靠左

f"價格 2 為 {print_2:>10.2f} \n" # 靠右
f"價格 3 為 {print_3:^10.2f}") # 置中

