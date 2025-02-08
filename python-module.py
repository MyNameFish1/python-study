#可以从python文档和python标准库中引入模块
#a//b 是除完后向下取整的意思
#引入statistics 模块
import statistics
print(statistics.median([69,124,-32,27,217]))
print(statistics.mean([19,-5,36]))
#使用模块中的median\mean函数

#引入模块的方式：import语句  引入后 可以用 模块名.函数名 来调用函数
#第二种 方式  from....import 语句   from 模块名 import 函数名1，函数名2。。。
from statistics import  median,mean
print(median([-19,5,36]))
print(mean([19,-5,36]))
#第二种的好处是每次用到函数或者变量时 不需要带上模块名字
#第三种 from ....import *   把。。。模块里所有函数全部调用 但是会出现调用的两个模块中有重名函数
#出现命名冲突
from statistics import  *
print( median([19,-5,36]))
print(mean([19,-5,36]))

#按住control点击函数名可以查看函数源代码

#引入第三方库的模块 引入前要先安装 安装后引入方法同上
