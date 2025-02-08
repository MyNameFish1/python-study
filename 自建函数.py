#定义函数代码
def calculate_sector_1 ():
    central_angle_1 = 160
    radius_1 = 30
    sector_area_1 = central_angle_1 /360 *3.14*radius_1 **2
    print(f"此处扇形面积为：{sector_area_1}")

def caculate_sector(central_angle,radius):
    sector_area  = central_angle/360 *3.14*radius **2
    print(f"扇形面积为：{sector_area}")
    return sector_area    #返回函数结果

sector_area_1 = caculate_sector(160,30)      #使用函数将返回结果赋值给变量

#BMI = 体重/（身高**2）

def BMI_caculate(weight,height):
    BMI=weight/(height**2)
    if BMI <= 18.5:
        print("偏瘦")
    elif BMI> 18.5 and BMI<=25 :
        print("正常")
    elif BMI >25 and BMI <= 30:
        print("偏胖")
    else:
        print("肥胖")

    return BMI

BMI = BMI_caculate(75,1.8)
print("您的BMI指数为："+str(BMI))


def BMI_caculate_1(weight,height):
    BMI=weight/(height**2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI<=25 :
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI

BMI = BMI_caculate_1(75,1.8)
print("您的BMI指数为："+str(BMI))
