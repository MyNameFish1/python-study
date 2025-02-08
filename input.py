name=input("我是你爸，你该叫我什么？\n")
print(name)
#input输入的均会被视为字符串 如果需要输入数字进行数值运算可以用强制类型转换
a=input("请输入数字：")
a=int(a)   #强制类型转换字符串类型为int类型
print(a+100000)
#整数不能和字符串连接在一起打印
#但可以进行强制类型转换
print("我知道我是你爸，你今年" + str(18)+"岁了")

#BMI = 体重/（身高**2）
user_weight = input("请输入你的体重（单位：kg）：")
user_height = input("请输入你的身高（单位：m）：")
BMI= int(user_weight)/(float(user_height)**2)
print(BMI)
print("您的bmi值为：" + str(BMI)