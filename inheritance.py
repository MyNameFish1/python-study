from unittest import skip


class cat:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
        self.has_tail = True

    def breathe(self):
        print(self.name+"呼吸")

    def poop(self):
        print(self.name +"在拉屎")

#Dry原则 不要重复 尽量少的重复代码
#继承可以创建有层次的类


#创建一个父类 eg.
class mammal :
    def __init__(self,name,sex):
        self.name = name               #共享属性
        self.sex = sex
        self.num_eyes = 2
    def breathe(self):                 #共享的方法
        print(self.name + "在呼吸" )

    def poop(self):
        print(self.name +"在拉屎")

#创建一个子类
class Human(mammal):   #人类子类继承mammal的属性 和方法
    def read(self):     #子类定义子类方法
        print(self.name + "在阅读")

class Cat(mammal):
    def scratch_sofa(self):
        print(self.name +"抓沙发")

cat1 = Cat("jojo","man!") #创建对象 调用父类方法 如果子类有父类同名方法，优先用子类方法
cat1.poop()

#人类和cat has_tail属性值不一样，不能只写在父类里
#但如果在子类中写构造函数 如：
class cat(mammal):
    def abc(self):
        self.has_tail = True

#那么只调用子类的构造方法 不继承父类的def方法
#为了不造成重复函数，可以在构造函数def中使用super方法
#eg.
  #  class cat(mammal):
   # def abc(self):
    #    super().__init__(name,sex)  #用super函数调用父类中name sex属性
     #   self.has_tail = True



#自己写一份
#人力系统
class Staff:
    def __init__(self,id,name):
        self.name =name
        self.id = id
    def print_info(self):
       # print(name + " " + id)
        print(f"员工名字：{self.name},工号：{self.id}")



class staff_long(Staff):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class staff_daily(Staff):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days

Man1 = staff_daily("张三","12138",300,30)
Man2 = staff_long("lisi","12111",5000)
print(Man1.calculate_monthly_pay())
print(Man2.calculate_monthly_pay())

Man1.print_info()
Man2.print_info()