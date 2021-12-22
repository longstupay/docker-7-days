name = input("请输入您的姓名：")
company = input("请输入您的公司名：")
title = input("请输入您的职位：")
email = input("请输入您的邮箱：")
info = f"""
您输入的结果如下：
尊敬的{name}，您好，您就职于{company}公司的{title}，
我们将会通过您的邮件{email}和您保持联系。
"""
print(info)