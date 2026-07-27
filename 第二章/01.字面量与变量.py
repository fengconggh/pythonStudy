# 字面量的写法
print(100)
print(3.14)
print(True)
print(False)
print("Hello Python")
print(None)

# bool类型涉及数字运算时,会自动转换为数字类型
print(1 + True) # 2
print(1 + False) # 1

# 变量的写法
num = 111.4
print(num)

num = num + 1
print(num)

# 动态类型语言,变量可以接收不同类型的值
num = "OK"
print(num) # OK

num = True
print(num)

# 案例
base = 20.7 # 基础播放量
incr = 50 # 每一个月的新增播放量
print("未来第一个月的播放总量:", base + incr) #未来第一个月的播放总量: 70.7

# 案例:一次性可以定义多个变量
base, incr = 100, 300.5
