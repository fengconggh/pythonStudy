# # 元组基本操作
# # 定义 元组名称 = (元素1, 元素2,...)
# tp = (123, 456)
# print(tp) # (123, 456)
# print(type(tp)) # <class 'tuple'>
# # 定义空元组
# tp = ()
# print(tp)
# tp = tuple()
# print(tp)
#
#
# # 索引访问
# tp = (123, 456, 3, 43, '323', 3, '323')
# print(tp[-1])
#
# # 切片
# print(tp[1::2])
#
# # count()统计元素个数
# print(tp.count(3))
# # index()查找元素位置
# print(tp.index('323'))

# # 元组组包与解包
#
# # 组包
# t1 = (1, 23, 5, 4, -1)
#
# # 解包
# a, b, c, d, e = t1
# print(a, b, c, d, e) # 1 23 5 4 -1
# a, *b, d, e = t1
# print(a, b, d, e) # 1 [23, 5] 4 -1
#
# # 案例,交换a, b的位置
# a = 1
# b = 2
# a, b = b, a # 解包与组包操作
# print(a, b)

# 案例一：
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 1.计算每个学生的总分、各科平均分,然后一并输出出来。
for student in students:
    print(f"{student[0]}-{student[1]}的总分：{sum(student[2:])}，各科平均分：{(sum(student[2:]) / (len(student[2:]))):.2f}")
# 2.统计各科成绩的最低分、最高分、平均分,并输出。
shuxue = [student[2] for student in students]
yuwen = [student[3] for student in students]
yingyu = [student[4] for student in students]
print(f"数学最低分{min(shuxue)}，最高分{max(shuxue)}，平均分{sum(shuxue) / len(shuxue)}")
print(f"语文最低分{min(yuwen)}，最高分{max(yuwen)}，平均分{sum(yuwen) / len(yuwen)}")
print(f"英语最低分{min(yingyu)}，最高分{max(yingyu)}，平均分{sum(yingyu) / len(yingyu)}")
# 3.查找成绩优秀（平均分大于90）的学生,并输出。
for student in students:
    if sum(student[2:])/len(student[2:]) > 90:
        print(f"{student[1]}的平均成绩超过了90")
