#需要打开 和关闭文件
with open("C:\\Users\\Administrator\\Desktop\\new.txt","w",encoding="utf-8") as f :   #如果文件不存在  程序会自动在该路径创建一同名文件
    #如果文件存在, W模式 会把源文件内容清空。
    f.write("hello! \n")
    f.write("YO!")
#如果只想在原有文件后面添加内容，用”a“模式 表示附加内容
with open("C:\\Users\\Administrator\\Desktop\\new.txt","a",encoding="utf-8") as f :   #如果文件不存在  程序会自动在该路径创建一同名文件
    f.write("hello! \n")
    f.write("YO!")
    #a 和w一样 若文件不存在 直接创建
    #a和w模式都不能直接用read读取
    #r+ ，a+模式同时支持读写（r+为覆盖写 a+为追加写

with open("C:\\Users\\Administrator\\Desktop\\new.txt","a+",encoding="utf-8") as f :
    print(f.read())
    f.write("666")


