#assert  后面跟上布尔表达式
assert len("hi") == 2   #如果表达式正确 无事发生
assert  1+2 > 6                  #如果表达式有问题 直接报错 AssertionError 断言错误   直接停止运行

assert  "a" in ["b","c"]

#测试用例的库 unittest
import unittest
#一般把测试代码放到独立文件里
#比如在my_calculator中定义函数  在测试文件里引入unittest包后再引入my_calculator文件中的函数
from my_calculateor import my_adder     #前面是文件名 后面是类名

class TestMyAdder(unittest.TestCase):    #定义一个测试类  当unittest.TestCase 的子类 继承功能
    def  test_positive_with_positive(self):
        self.assertEqual(my_adder(5,3),8)      #与assert功能类似但不会中断程序 第一个参数和第二个参数相等则通过 不然不通过
    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5,3),-2)

    #写好测试用例后 在编辑器终端输入python -m unittest

#unittest.TestCase类常见测试方法
# 方法1 assertEqual(A,B) 类似于assert A==B
#assertTrue(A) 类似于 assert A is True
#assertI(A，B)      assert A in B
#本质上 assertTrue可以代替所有方法 eg。 assertTrue(2 not in [1,3-1])    等价于 assertNotIn(2,[1,,3-1])  判断2是不是在[1,3-1]这个列表里
#但更推荐针对性方法 针对性方法会给出详细失败原因 泛用的方法只有false is not true