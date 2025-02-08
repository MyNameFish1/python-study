#运算顺序和平时数学一样
#优先级：()  **(乘方）  */  +-
import math
sin1=math.sin(1)
print(sin1)

a=-1
b=2
c=3
x=(-b+(b**2 - 4*a*c)**(1/2))/2*a
x2=(-b-(b**2 - 4*a*c)**(1/2))/2*a
print(x , x2)