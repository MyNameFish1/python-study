#for 变量名 in 迭代对象：
#eg.
temperature_list = [36.4,36.6,37.0,37,38,39,38,37,38]
for temperature in temperature_list:
    if temperature >=38:
        print(temperature)
        print("完辣！")

temperature_dict = { "111":36.4,"112":36.6,"113":38.8}
temperature_dict.keys()         #返回所有键
temperature_dict.values()       #返回所有值
temperature_dict.items()        #返回所有键值对  在for循环时变量会被赋值为键和值组成的元组

for staff_id,temperature in temperature_dict.items():  #键赋值给staff_id 值赋值给temperature
    if temperature >= 38:
        print("\n"+staff_id +"完辣！")

#同上

for temperature_tuple in temperature_dict.items():    #temperature_tuple 是一个元组
    staff_id = temperature_tuple[0]     #把staff_id 赋值给元组0号位
    temperature = temperature_tuple[1]   #赋值给1号位
    if temperature >= 38:
        print("\n" + staff_id +"完辣！")

#range函数 eg. range(5,10)整数数列 5表示起始值为5 10表示结束值为10 结束值不在数列范围内
#eg.
for i in range(5,10):
    print(i)
    #i被依次赋值为5-9
#range(5,10,2)  2 表示步长 每次跨两个数字 不指明时默认为1
for i in range(1,10,2):
    print(i)
    #打印1，3，5，7，9

total = 0
for i in range (1,101):
    total = total + i
print(total)



