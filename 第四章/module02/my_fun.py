__all__=["PI", "out_line"]
PI = 3.14

def out_line(amount: int):
    print("-" * amount)



# 当直接指定此模块，如下代码会执行，导入模块时不会执行
if __name__ == '__main__':
    out_line(10)
    print(__name__)
# 直接运行： __main__
# 导入模块：第四章.module02.my_fun