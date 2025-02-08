#字典
contacts = {"xiaomin":"13100000000","abc":"13200000000"} #在字典里用多个键值对 用花括号包住 键和值之间用用好表示对应 键值对之间用逗号分隔
#要获取某个键的值 在字典名后面跟方括号
contacts["xiaomin"]
#键的类型必须不可变 列表属于可变数据类型 字符串 整数 浮点数 等可以作为键 列表不能
#元组()用圆括号 列表用方括号
tuple=("a","b")  #元组不可变 不能用append ，remove操作   元组可以作为键
#eg.
contact1 = {("zhangwei",23):"114514",("zhangwei",50):"233333"}
#查询时可以用整个元组作为键
print(contact1[("zhangwei",23)])
#字典和列表都是可变的 可以添加和删除键值对
#也可以这样赋值
slang_dict = {}
slang_dict["双减"] = "减轻学生作业负担和校外培训负担"
slang_dict["躺平"] = "指人在面对压力时主动放弃不做反抗"
query = input("请输入你想要查询的流行语：")
if query in slang_dict:
    print("您查询的这个词 "+ query+ " 含义如下")
    print(slang_dict[query])
else:
    print("暂未收录")
    print("当前词典收录的词条数目为" + str(len(slang_dict)) + "条")