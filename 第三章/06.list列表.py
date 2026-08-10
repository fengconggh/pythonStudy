# # 定义
# list1 = [55, 555, 342, 121, 898]
# # 新增
# list1.append(22)
# print(list1) # [55, 555, 342, '121', 898, 22]
# list1.extend(list1)
# print(list1) # [55, 555, 342, '121', 898, 22, 55, 555, 342, '121', 898, 22]
# list1.insert(0, 789)
# print(list1)
#
# # 删除
# list1.remove(22) # 删除第一个值为22的元素
# del list1[4] # 删除索引为4的元素
# print(list1)
#
# print("---------pop---------")
# list1.pop(4)
# print(list1)
# # list1.clear()
# print(list1) # []
#
# # 查询
# print(list1.index(55, 3, 5)) # 返回第一个值为55的索引，给定的范围内如果没有回报错
# print(list1.count(55))
# # 排序
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# # 复制
# list2 = list1.copy()
# print(list2)
# # 组合
# print(list1 + list2)
# print(*list2)

# # 案例一：
# list1 = [15,65,98,447,3,66,55,449,-58,99,0]
# # 排序
# list1.sort()
# print(f"排序后为：{list1}")
# print(f"最大值为：{list1[-1]}")
# print(f"最大值为：{max(list1)}")
# print(f"最小值为：{list1[0]}")
# print(f"最小值为：{min(list1)}")
# print(f"平均值为：{sum(list1) / len(list1)}")

# 案例二：
# num_list1 = [19,23,54,65,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# # 合并
# num_result = num_list1 + num_list2
# print(num_result)
# num_result = [*num_list1, *num_list2]
# print(num_result)
# #去重
# new_list = []
# for i in num_result:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# 案例三：
# 列表推导式
# 生成1-20的平方列表
res_list = [i*2 for i in range(1, 21)]
print(res_list)

# 生成1-20中所有偶数的平方列表
res_list = [i*2 for i in range(1, 21) if i % 2 == 0]
print(res_list)
