#while A：
    #B
#measure_brightness函数返回当前测量的天空亮度
#measure_brightness = input("输入亮度：")
#while measure_brightness()>= 500 :
    #拍照片
 #   take photo()

list1 = ["你" , "hao" , "ma", "xiong","di"]
for char in list1:
    print(char)

for i in range(len(list1)):  #适用于有明确循环对象和次数的时候更方便
    print(list1[i])

i = 0
while i < len(list1):   #while 适用于 循环次数未知的情况
    print(list1[i])
    i = i + 1


#写一个对用户输入求平均值的计算器
count = 0
total = 0
user_input = input("请输入数字，输入完后输入q退出")
while user_input != "q":    #条件判断是在循环体执行前判断，因此输入的user_input必须是在上一次判断最后 或者首次判断之前输入
    num = float(user_input)      #否则输入q时会无法将q转换为字符串
    total+= num
    count += 1
    user_input = input()
if count == 0:
   print(total)
else:
    print(total/count)

