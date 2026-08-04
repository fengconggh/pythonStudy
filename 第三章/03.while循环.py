# 循环
## while
i = 0
while i < 10:
    print("人生苦短,我用Python~")
    i += 1
    if i > 5:
        print(10000)
        break
else:
    print("循环结束")


## 案例:计算1~100之间所有的偶数的累加之和
result = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(f"result: {result}")
