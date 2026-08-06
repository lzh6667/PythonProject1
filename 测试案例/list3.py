#生成1——20的平方列表
#从如下数字列表中提取所有的偶数组成一个心灵的列表
#方式1
num_list=[]
for i in range(1,21):
    num_list.append(i**2)
print(num_list)
#方式2 列表推到式
#就是按照一定的规则快速生成一个列表的方法
num_list2=[i**2 for i in range(1,21)]
print(num_list2)

#数列推到狮子中的条件判断
num_list3=[12,33,44,55,66,90]
new_list=[i**2 for i in num_list3 if i%2==0]
print(new_list)