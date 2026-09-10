"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入
完成后修改该商品信息。
3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商
品数量:xxx"。
5.退出购物车
"""
#购物车类

class Goods:
    def __init__(self,name,price,num):
        self.name=name
        self.price=price
        self.num=num
    def __str__(self):
        return {f"商品名称{self.name} 商品数量{self.num}价格{self.price}"}
    #对于添加物品这一块我有话想说：

    def update_goods (self,name=None,price=None,num=None):
        self.name=name
        self.price=price
        self.num=num
class Manage_cart :
    
    def __init__(self):
        self.shoping_cart=[]
    def add_cart(self):
        name =input("请输入商品的名称")
        for s in self.shoping_cart:
            if name==s.name:
            #或者这样写 Goods=Goods(name,price,num)
                print("当前商品已存在，请检查后再添加")
                return
        price=input("请输入商品的价格")
        num=input("请输入商品的数量")
        Good=Goods(name,price,num)
        self.shoping_cart.append(Good)
        print("添加商品成功")
    def update_cart(self):
        name=input("请输入需要修改的商品名称")
        for s in self.shoping_cart:
            if name==s.name:
                name =input("请输入商品的名称")
                price=input("请输入商品的价格")
                num=input("请输入商品的数量")
                s.update_goods(name,price,num)
                print("修改成功")
        print("修改失败")
        return        
    def del_cart(self):
        name=input("请输入需要删除的商品名称")
        for s in self.shoping_cart:
            if name==s.name:
                self.shoping_cart.remove(s)
                return
        print("删除失败")
    def search_cart(self):
        for s in self.shoping_cart:
            print(f"商品名称{s.name},商品价格{s.price},商品数量{s.num}")
        if not self.shoping_cart:
            print("购物车中没有商品")
    def run(self):
        system_version="1.0"
        while True:
            print(f"欢迎使用购物车管理系统,版本号{system_version}")
            print("""
            1.添加商品
            2.修改商品
            3.删除商品
            4.查询商品
            5.退出
            """)
            choice=int(input("请输入需要的功能"))
            match choice:
                case 1:
                    self.add_cart()
                case 2:
                    self.update_cart()
                case 3:
                    self.del_cart()
                case 4:
                    self.search_cart()
                case 5:
                    print("感谢您的使用,再见")
                    break
                case _:
                    print("输入错误")

cart=Manage_cart()
cart.run()              

       
       