#预判错误
#异常类型 IndexError ZeroDivisionError除零错误 找不到文件错误 类型错误。。。。。。
#异常类型错误多
#捕捉异常
try:
    user_weight =float(input("请输入你的体重（KG）："))
    user_height =float(input("请输入你的身高（CM）"))
    user_BMI = user_weight / user_height **2

except ValueError:                           #数据类型错误 捕捉到后会报错
    print("输入不合理 请重新运行程序 输入正确数字")
except ZeroDivisionError:                 #除零错误
    print("身高不能为零 请重新输入 ")
except :                                     #希望所有错误都被捕捉返回直接用except
    print("未知错误 重新运行")

    #try except 语句会从上到下依次判断运行 捕捉到错误后后续不再运行 类似if elif

    #except后放置else语句 当没有错误时会运行  finally 无论错误与否都会运行
else:
    print("您的bmi值时 " + str(user_BMI) )
finally:                                     #不管是有没有错误还是错误没捕捉程序炸了，都会运行
    print("程序运行结束")



