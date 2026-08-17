# 函数
# def out_line():
#     print("----------------")
#
# out_line()

# 案例一：
# def triangle_area(base, height):
#     """
#     计算三角形的底和高计算三角形的面积
#     :param base: 底
#     :param height: 高
#     :return: 三角形的面积
#     """
#     return round(base * height / 2, 2)
#
# print(triangle_area(10, 20))

# 案例二：
# def count_vowels(text: str):
#     """
#     计算字符串中元音字母的个数
#     :param text: 字符串
#     :return: 元音字母个数
#     """
#     a = sum(1 for s in text.lower() if s in 'aeiou')
#     return a
#
# print(count_vowels('aaaaa'))

# 案例三：
def score_fun(score_list):
    """
    计算最高成绩、最低成绩、平均成绩
    :param score_list: 成绩列表
    :return: 最高分，最低分，平均分
    """
    return max(score_list), min(score_list), round(sum(score_list) / len(score_list), 1)

print(score_fun([580, 666, 740, 320, 158]))