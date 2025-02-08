#格式化字符串
contacts = ["laoyu","laolin","laozhu","laocheng","laoli","laowang","帽子有"]
for name in contacts :
    message_contents = name + "新年好，给我打钱，\n打快点"
    print(message_contents)

#format方法"
year=[2010,2011,2012,2013]
name = ["zhu","niu","ji","gou"]
i=0
while i <=3:
    message_contents = """
    你好{name1},今年是{year1}，给我打钱""".format(name1=name[i],year1=year[i])
    print(message_contents)
    i+=1

#f字符串效果同上
i=0
while i <=3:
    message_contents = f"""
    你好{name[i]},今年是{year[i]}，给我打钱"""
    print(message_contents)
    i+=1

#format 可以直接打印数字 不用手动转换成字符串打印
gpa_dict = {"小明":3.251,"小花":3.855,"小李":2.666}
for name,gpa in gpa_dict.items():
    print("{0}你好，你的绩点为：{1:.2f}".format(name,gpa))  #.2f打印出的保留两位小数

#f字符串同上