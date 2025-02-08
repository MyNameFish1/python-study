#字符串str “abc” ‘’    len函数可以得到字符串长度
a=len("abc")
print(a)
b=len("\n")    #转义符\存在时 完整的一个转义才为一个长度 eg.
print(b)
c="hellp"[2]   #字符串后添加索引得到单个字符 索引从0开始数
print(c)
#整数int 6 -1
#浮点数float 6.0

#布尔值bool True False
                     #只有两个值
#空值NoneType None 完全没有值 非0
#不确定对象类型时候可以用type()函数 返回该对象的类型
d=type(False)
print(d)
