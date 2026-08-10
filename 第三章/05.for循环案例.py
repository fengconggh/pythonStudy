# 案例一：打印9*9乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i >= j:
#             print(f"{i} * {j} = {i * j}", end="\t")
#     else:
#         print()
import random

# 案例二：完成登录操作
# while True:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "" or password == "":
#         print("用户名或密码不能为空，请重新输入！")
#         continue;
#
#     if username == "admin" and password == "666888":
#         print("登录成功！")
#         break;
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功！")
#         break;
#     else:
#         print("用户名或密码错误，请重新输入！")
#
# print("进入首页！")

# 案例三：猜数字游戏
num = random.randint(1, 100)
while True:
    inputNum = int(input("请输入数字："))
    if num < inputNum:
        print("输入的数字大了！")
        continue
    elif num > inputNum:
        print("输入的数字小了！")
    else:
        print("恭喜你，猜对了！")
        break

