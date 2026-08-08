"""通过控制台菜单与用户交互。具体功能如下:
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息
3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
5.退出购物车"""

#1。制作菜单

print("1.欢迎使用购物车管理系统")   


shopping_cart={}
while True:
    menu ="""
########### 购物车系统 #############
#           1.添加购物车           #
#           2.修改购物车           #
#           3.删除购物车           #
#           4.查询购物车           #
#           5.退出购物车           #
##################################
"""
    print(menu)
            #执行的操作
    choice=int(input("请输入您的选择1-5："))
    match choice:
        case 1:
            print("当前执行的是添加操作")
            shopping_name=input("请输入商品名称：")
            shopping_price=float(input("请输入商品价格："))
            shopping_num=int(input("请输入商品数量："))
            if shopping_name not in shopping_cart:
                shopping_cart[shopping_name]={"price":shopping_price,"number":shopping_num}
            else:
                print("该商品已存在请从新输入")
        case 2:
            print("当前执行的是修改操作")
            goods_name = input("请输入修改的商品名称：")
            goods_price = float(input("请输入修改的商品价格："))
            goods_num = int(input("请输入修改的商品数量："))
            if goods_name not in shopping_cart:
                print("当前商品未添加无法进行修改")
            else:
                shopping_cart[goods_name]={"price":goods_price,"number":goods_num}
        case 3:
            print("当前执行的是删除操作")
            goods_name=input("请输入需要删除商品的名称")
            if goods_name not in shopping_cart:
                print("当前商品不存在")
            else :
                shopping_cart.pop(goods_name)
               #del shopping_cart[goods_name]
        case 4:
            if  not shopping_cart:
                print("当前列表为空")
            else:
                print("当前执行的是查询操作")
                for goods_name in shopping_cart:
                    goods_info=shopping_cart[goods_name]
                    print(f"商品名称:{goods_name} 商品价格:{goods_info['price']} 商品数量:{goods_info['number']}")
        case 5:
            print("现在进行的是退出操作")
            print("感谢您的使用")
            break
        case _:
          print("输入错误，请重新输入")
          