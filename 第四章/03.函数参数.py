# 不定长参数 - 可变参数
# 位置传递
# def calc_data(*args):
#     print(type(args)) # <class 'tuple'>
#     return sum(args)
#
# data = calc_data(11, 22, 334)
# print(data)

# 关键字传递
# def calc_data(*args, **kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     if kwargs.get("aaa") is not None:
#         print(kwargs.get("aaa"))
#     else:
#         print("11111111")
#
#
# calc_data(111, 2222, aaa1=444)

# 参数类型可以传函数
def add(x, y):
    return x + y;

def subs(x, y):
    return x - y

def calc(x, y, oper):
    return oper(x, y)

print(calc(1, 3, add)) # 4
print(calc(1, 3, subs)) # -2