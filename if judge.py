mood_index = int(input("对象今天的心情："))
if mood_index >= 60:
    print("恭喜你今晚应该可以打游戏，去吧")
else :
    print("你敢打你就死定了。")

stayornot = bool(input("她今天在家吗"))

if mood_index <=60:
    if stayornot:
        print("you'll die")

else:
    print("freedom!")

if mood_index > 60:
    pass
elif mood_index >50 & mood_index <= 60:
    pass
else:
    print("6")
