#写法一 直接通过将两个数组合并进行接入
num_list1=[19,20,11,22,33,44,55]
num_list2=[19,2,3,4,5,6,7,8,9,10]
for num in num_list1:
    num_list2.append(num)
print(f"合并之后的数组{num_list2}")
new_list=[]
for num in num_list2:
    new_list.append(num)##
print("去除重复元素的数组",new_list)
#写法2 通过解包租宝解决
num_list1=[19,20,11,22,33,44,55]
num_list2=[19,2,3,4,5,6,7,8,9,10]


new_list=[*num_list1,*num_list2]
print("组合后的数组",new_list)
for num in num_list2:
    new_list.append(num)##
print("去除重复元素的数组",new_list)
#写法3 直接组合
num_list1=[19,20,11,22,33,44,55]
num_list2=[19,2,3,4,5,6,7,8,9,10]

print(f"合并之后的数组{num_list2}")
new_list=num_list1+num_list2
for num in num_list2:
    new_list.append(num)##
print("去除重复元素的数组",new_list)
print("你好")