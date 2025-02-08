# and or not   eg. x>5 and x<10  and 连接两个或以上的对象 只要有一个为false 全为false
# or 连接两个或以上的对象 只要有一个为true 整个条件为true
#not  eg.not a>b 若a>b为true 则返回false 反之同理、
#逻辑运算可以用括号改变运算顺序 not(x>5 and ( x<10 or x==12))
#用逻辑运算写条件运算
if(house_work_count > 10 and red_envelop_count >1 and shopping_count > 4 and not has_been_angry):
    print("waiting switch!")
else:
    print("waiting witch....")