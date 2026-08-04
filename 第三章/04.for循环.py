# range
# 用法一：range(end) -> 获取一个从0开始，到end结束的数字序列（不包含end本身）
r = range(5)
for i in r:
    print(i, end=" ") # 0 1 2 3 4
else:
    print("")
# 用法二：range(start, end) -> 获取一个从start开始，到end结束的数字序列（不包含end本身）
r = range(2, 5)
for i in r:
    print(i, end=" ")
else:
    print("")
# 用法三：range(start, end, step) -> 获取一个从start开始，到end结束的数字序列，step为步长（不包含end本身）
r = range(2, 5, 2)
for i in r:
    print(i, end=" ")
else:
    print("")