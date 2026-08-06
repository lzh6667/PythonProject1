"""根据如下提供的学生成绩单，完成如下需求:
1.计算每个学生的总分、各科平均分，然后一并输出出来。
2.统计各科成绩的最低分、最高分、平均分，并输出。
3.查找成绩优秀(平均分大于90)的学生，并输出。
"""

# 学生成绩单测试数据 (元组列表：学号, 姓名, 语文, 数学, 英语)
students = [
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
]
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total= s[2]+s[3]+s[4]
    avg= total/3
    print(f"{s[0]}\t\t{s[1]}\t\t{s[2]}\t\t\t{s[3]}\t\t\t{s[4]}\t\t\t{total}\t\t\t{avg:.2f}")
for s in students:
    math_score =[s[3] for s in students]
    chinese_score =[s[2] for s in students]
    english_score =[s[4] for s in students]
    math_min=min(math_score)
    math_max=max(math_score)
    math_avg=sum(math_score)/len(math_score)
    english_min=min(english_score)
    english_max=max(english_score)
    english_avg=sum(english_score)/len(english_score)
    chinese_min=min(chinese_score)
    chinese_max=max(chinese_score)
    chinese_avg=sum(chinese_score)/len(chinese_score)
print(f"语文最低分是：{chinese_min}，最高分是：{chinese_max}，平均分是：{chinese_avg:.2f}")
print(f"数学最低分是：{math_min}，最高分是：{math_max}，平均分是：{math_avg:.2f}")
print(f"英语最低分是：{english_min}，最高分是：{english_max}，平均分是：{english_avg:.2f}")

for s in students:
    total= s[2]+s[3]+s[4]
    avg= total/3
    if avg>90:
        print(f"{s[0]} {s[1]}平均分为：{avg:.2f} 成绩优秀")
