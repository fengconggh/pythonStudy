# 邮箱案例
# 方式1
# str_mail = input("请输入邮箱地址：")
# if str_mail.count('.') >= 1 and str_mail.count('@') == 1:
#     print("邮箱格式正确！")
# else:
#     print("邮箱格式错误！")

# 方式2
str_mail = input("请输入邮箱地址：")
if '.' in str_mail and str_mail.count('@') == 1:
    print("邮箱格式正确！")
else:
    print("邮箱格式错误！")