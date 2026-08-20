# lambda表达式
# x_y = lambda x, y: x + y
#
# print(x_y(1, 2))
#
#
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# data_list.sort(key=lambda item : len(item), reverse=True)
# print(data_list)
# # ['JavaScript', 'Python', 'Jack', 'Java', 'Rust', 'C++', 'PHP', 'Go', 'C']
#
# data_list.sort(key=len)
# print(data_list)
# # ['C', 'Go', 'C++', 'PHP', 'Jack', 'Java', 'Rust', 'Python', 'JavaScript']


# 案例一：计算阶乘
# def factorial_cun(n):
#     if n > 1:
#         return n * factorial_cun(n - 1)
#     else:
#         return n
#
# print(factorial_cun(3))

# 案例二：
goods_list = ({"name":"水壶", "price": 300, "amount": 20})

def calc_order_fee(*goods, privilege={"couponVal": 0, "scoreValue": 0}, shippingCost=0.0):
    """
    计算订单总价格
    :param goods: 商品信息
    :param privilege: 优惠信息
    :param shippingCost: 运费信息
    :return: 订单总价
    """
    # 1. 计算商品总金额
    goods_fee = sum(int(good.get("price")) * int(good.get("amount")) for good in goods)
    print("商品总价：", goods_fee)

    # 2 计算抵扣金额
    discount = 0
    if goods_fee > 5000:
        # 2.1 计算优惠券抵扣
        couponVal = int(privilege.get("couponVal"))
        if (couponVal > goods_fee):
            discount += goods_fee
        else:
            discount += couponVal
        print("优惠券抵扣：", discount)

    goods_fee -= discount

    discount = 0
    if goods_fee > 5000:
        # 2.2 计算积分抵扣
        scoreVal = int(privilege.get("scoreValue")) // 100
        if (scoreVal > (goods_fee - discount)):
            discount = goods_fee
        else:
            discount += scoreVal
        print("抵扣总金额：", discount)


    goods_fee -= discount

    # 3. 计算总金额
    sum_fee = goods_fee + shippingCost;
    print("订单总金额为：", sum_fee)

calc_order_fee({"name":"鼠标", "price": 188, "amount": 2}, {"name":"键盘", "price": 388, "amount": 1},{"name":"手机", "price": 6999, "amount": 1},
               privilege={"couponVal": 10, "scoreValue": 4000}, shippingCost=9.9)

# 商品总价： 7763
# 优惠券抵扣： 10
# 抵扣总金额： 40
# 订单总金额为： 7722.9


# 类型注解

def temp_fun(a: int, b: str):
    print(a)
    print(b)


































