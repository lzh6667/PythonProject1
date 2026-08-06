#输入是个数字并把数字按照大小排序并且输出最大最小值和平均值
num_list=[]
#输入数据
for i in range(10):
    num=int(input("enter number:"))
    num_list.append(num)
print(num_list)
num_list.sort()
print("最大值是:",num_list[0])
print("最小值是：",num_list[-1])
print("平均值是：",sum(num_list)/len(num_list))