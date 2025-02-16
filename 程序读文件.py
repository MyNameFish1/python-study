#先打开目标文件
##模式“r”只读 “w”只写
#open("路径"，“模式")
#eg
f=open("C:\\Users\\Administrator\\Desktop\\666.txt","r",encoding="utf-8")      #python默认\符号为转义符 因此windows系统文件路径中的\要再用一个\进行转义 因此为\\
#打开文件后会返回一个文件对象 赋值给f 可以进行后续操作
print(f.read())     #读取文件内容 返回全部文件内容的字符串
print(f.readline())    #读取一行的内容 返回字符串 以换行符为结尾 调用一次读取一行
#如果不知道有几行 就用while函数
line = f.readline()
while line != "":        #设置条件 判断当前行是否为空
    print(line)         #不为空打印当前行
    line = f.readline()  #读取下一行

print(f.readlines()) #会读取全部文件内容 把每行文件作为列表元素返回 一般和for循环结合使用
lines = f.readlines()
for line in lines:
    print(line)            #打印当前行



#读完文件要关闭文件 释放系统资源  f.close()
f.close()


with open("C:\\Users\\Administrator\\Desktop\\666.txt") as f:     #不需要关闭文件的方式 ,但所有操作都要在：内部进行 因此需要缩进
    print(f.read())

File = open("C:\\Users\\Administrator\\Desktop\\666.txt","r",encoding="utf-8")
content =File.read()
print(content)
f.close()

with open("C:\\Users\\Administrator\\Desktop\\666.txt","r",encoding="utf-8") as File:
    content = File.read()
    print(content)

with open("C:\\Users\\Administrator\\Desktop\\666.txt","r",encoding="utf-8") as File:
    print(File.readline())

with open("C:\\Users\\Administrator\\Desktop\\666.txt","r",encoding="utf-8") as File:
    print(File.readlines())         #返回列表 结尾换行符也被读取作为文件一部分

#和for循环结合使用
with open("C:\\Users\\Administrator\\Desktop\\666.txt", "r", encoding="utf-8") as File:
    lines = File.readlines()
    for line in lines:
        print(line)

