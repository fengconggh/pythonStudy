# match...case
a = int(input("请输入:"))
b = 2
match a:
    case 1:
        print("测试1")
    case 2 if b > 2:
        print("测试2")
    case 3 | 4:
        print("测试3或4")
    case _:
        print("默认行为!")