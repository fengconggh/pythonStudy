# 全局变量与局部变量
num = 100

def num_fun():
    # 局部变量，与外部的全局变量不是一个
    # 场景一：
    # num = 1000
    # print(num) # 1000
    # 场景二：
    global num
    num = 10000
    print(num) # 10000

num_fun() # 1000
print(num) # 100   10000
