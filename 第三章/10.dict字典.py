# 字典
# # 定义  key 不能重复，如果重复，后面的值会覆盖前面的值
# dict1 = {"张三": 111, "李四": 222}
# print(dict1)
# print(type(dict1))
#
# # key 必须是不可变类型 str int float tuple
# dict2 = {"张三": 111, "李四": 222, 0: 3, 0.5: 4, (2, 3): 555}
# print(dict2)
#
# # 访问
# print(dict2["李四"])
# dict2["李四"] = 444 # 可以修改
# print(dict2)
#
# print(dict1.keys()) # dict_keys(['张三', '李四'])
# print(dict2.values()) # dict_values([111, 444, 3, 4, 555])
# print(dict2.items()) # dict_items([('张三', 111), ('李四', 444), (0, 3), (0.5, 4), ((2, 3), 555)])
# for dc in dict2.items():
#     print(type(dc)) # <class 'tuple'>
#
# for k, v in dict1.items():
#     print(f"{k} : {v}")

# 案例一：
print("欢迎使用购物车管理系统！")
print()
print("########## 购物车系统 ##########")
print("#       1. 添加购物车          #")
print("#       2. 修改购物车          #")
print("#       3. 删除购物车          #")
print("#       4. 查询购物车          #")
print("#       5. 退出购物车          #")
print("########## 购物车系统 ##########")
products = {}
while True:
    oper = input("请选择要执行的操作（1-5）：")
    match oper:
        case "1":
            goods_name = input("请输入商品名称：")
            if goods_name in products:
                print("当前商品已存在，请重新输入：")
                continue
            goods_price = input("请输入商品价格：")
            goods_amount = input("请输入商品数量：")
            products[goods_name] = {"price": goods_price, "amount": goods_amount}
            print("操作成功！")
        case "2":
            goods_name = input("请输入商品名称：")
            if goods_name not in products:
                print("当前商品不存在，请重新输入：")
                continue
            goods_price = input("请输入商品价格：")
            goods_amount = input("请输入商品数量：")
            products[goods_name] = {"price": goods_price, "amount": goods_amount}
            print("操作成功！")
        case "3":
            goods_name = input("请输入商品名称：")
            if goods_name not in products:
                print("当前商品不存在，请重新输入：")
                continue
            del products[goods_name]
            print("操作成功！")
        case "4":
            for goods_name in products.keys():
                print(f"查询结果：商品名称：{goods_name}，商品价格：{(products[goods_name]).get("price")}，商品数量：{products[goods_name]["amount"]}")
            print("操作成功！")
        case "5":
            print("已退出！")
            break
        case _:
            print("不支持的操作类型，请重新输入：")
