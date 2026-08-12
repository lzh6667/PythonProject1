"""定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)
优惠(优惠券、积分抵扣)、运费
息计算订单的总金额。
具体规则如下:
优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣
"""

def calc_order_cost(*args,coupon=0,score=0,express=0):
    """
    :param args:  商品信息 (商品名、价格、数量) —————>如（“鼠标”，188，2）
    :param coupon: 优惠券金额
    :param score: 积分
    :param express: 运费
    :return: 订单总金额
    """

    #1.计算商品总金额
    total_price=[goods[1]*goods[2] for goods in args]
    total_cost=sum(total_price)
    #2.减扣优惠卷
    if total_cost>=5000 and coupon<=total_cost:
        total_cost-=coupon
    #3.减扣积分抵扣
    if total_cost>=5000 and score//100<=total_cost:
        total_cost-=score//100
    #4.添加运费
    total_cost+=express
    return total_cost
    
print(calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9))