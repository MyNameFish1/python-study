#面向对象编程  先考虑各个对象的性质
#定义ATM类
class ATM:
    def __init__(self,编号,银行,支行):    #ATM类的构造函数，初始化类实例 self 是类实例引用 用于访问类属性和方法 编号等为参数 传递创建对象时需要的数据
        self.编号 = 编号                 #属性赋值
        self.银行 = 银行                 #self.银行 = 银行：将传入的 银行 参数赋值给类实例的 银行 属性。
        self.支行 = 支行

#创建两个ATM对象
atm1 = ATM("001","招商银行","南苑支行")
atm2 = ATM("002","中国银行","南苑支行")
print(atm1.编号)  #直接用对象.属性获取对应属性

#面向对象具体语法
#下划线命名 适用于变量名 eg. user_name
#Pascal命名 适用于类名 首字母大写分隔单词 例子UserAccount CustomerOrder
class CuteCat:
    #定义类的代码
    #属性等
    def __init__(self): #def 构造函数定义实例对象属性 必须被定义为_init_()  () 中可以放任意数量参数 第一个参数永远被self占用 表示对象自身
        self.name = "Lambton"         #self.name 给self这个对象的name属性赋值

#创建对象  类定义属性
cat1 = CuteCat()  #调用CuteCat()创建对象时 _init_ 方法自动运行self自动传入不需要手动输入
print(cat1.name)

#从参数获取name的值
class CuteCat:
    def __init__(self,cat_name):     #括号里面传入cat_name
        self.name = cat_name

cat2 = CuteCat("Jojo")               #定义类的时候传入一个name属性
print(cat2.name)


#自己写一个
class 人类:
    def __init__(self,skin_color,gender,gender_identity):
        self.color = skin_color
        self.gender = gender
        self.identity = gender_identity

human1 = 人类("black ","male ","Walmart shopping bag ")
print(human1.color+human1.gender+human1.identity)
print(f"这是个{human1.gender}{human1.color}人，但他认为自己是{human1.identity}")



#类定义方法
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):  #self 可以在方法里获取和修改方法绑定的对象的属性
        print("妙" * self.age)         #获取self对应的属性

    def think(self,content):
        print(f"小猫{self.name}在思考{content}")
cat1 = CuteCat("Jojo",10,"orange")

cat1.think("现在是抓沙发还去抓纸箱")
cat1.speak()




#自定义一个学生类
class Student:
    def __init__(self,name,number,chinese_scores,english_scores,math_scores):
        self.name = name
        self.number = number
        self.chinese = chinese_scores
        self.english = english_scores
        self.math = math_scores

    def Scores(self):
        print(f"学生 {self.name} 学号为 {self.number} 的语数外成绩分别为 {self.chinese} {self.math} {self.english}")

xiaoming = Student("明",114514,90,60,70)
xiaoming.Scores()


#另一种写法
class Student1:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.grades = {"语文":0,"数学":0,"英语":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade


    def Scores(self,course):
        print(f"学生 {self.name} 学号为 {self.number}的{course}{self.grades[course]}分 ")

chen = Student1("小曾",114514)
chen.set_grade("语文",60)
chen.Scores("语文")
