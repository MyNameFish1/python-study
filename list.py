#列表（可以放不同类的元素 字符串 浮点数整数都可以放一起  和其他语言不一样
shopping_list=[]
shopping_list=["键盘","键帽"]
shopping_list.append("显示器") #方法一般在操作对象后面加点 append可在列表后添加元素
print(shopping_list)
shopping_list.remove("显示器")   #remove 删除列表中的“”元素
print(shopping_list)
#列表可变 字符串等不可变
#eg.
s="hello"
print(s.upper())  #upper函数把原字符串全部大写输出
print(s)     #但原字符串没有改变
s=s.upper()   #只有通过赋值才能改变
print(s)     #新全大写字符串

#len函数 求列表长度
a=len(shopping_list)
print(a)
#索引
print(shopping_list[1])
#修改列表元素
shopping_list[1] = "牛"
print(shopping_list[1])
#min() max() 得列表最大最小值
