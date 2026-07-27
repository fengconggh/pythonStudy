# type() 获取指定字面量或变量的类型
print(type("Hello Python")) # <class 'str'>

print(type(10)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>

# isinstance() 判定数据是否是指定的类型
num = -100

print(isinstance(num, int)) # True
print(isinstance(num, float)) # False

# 字符串
# 定义字符串的三种方式
s1 = "Hello"
s2 = 'Python'
s3 = """
`1123
1232132
"""
print(s1)
print(s2)
print(s3)

# 转义字符 \' \" \n \t
msg = 'It\'s vary good'

# 字符串拼接
slogan = "子串1" "子串2"
print(slogan)
# +号可以用来拼接两个字符串,无法拼接非字符串,拼接前需转换为字符串
slogan2 = "子串1" + str(1)
print(slogan2)

# 字符串格式化1
s1 = "Hello"
s2 = "Python";
print("张三说%s,李四说%s" % (s1, s2))
# 字符串格式化2: f"内容{变量/表达式}"
print(f"李四说{s1}, 张三说{s2}")