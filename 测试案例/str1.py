##判断邮箱输入格式是否正确
mail =input("请输入您的邮箱")
if mail.count("@")==1 and mail.count(".")>=0:
    print("合法")
else:print("不合法")
