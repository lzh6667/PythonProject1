

students_dict = {}
while True:
    print("""
    ########### 教务管理系统 #############
#           1.添加学生信息           #
#           2.修改学生信息           #
#           3.删除学生信息           #
#           4.查询学生信息           #
#           5.显示所有学生信息        #
#           6.统计班级成绩            #
#           7.退出系统               #
##################################
    """)
    choice = int(input("请输入您的选择："))
    match choice:
        case 1:
            print("当前你进入的是添加学生信息系统")
            students_name=str(input("请输入学生姓名"))
            if(students_name in students_dict):
                print("当前学生已存在退出系统")
                break
            students_chinese_score=int(input("请输入语文成绩"))
            students_math_score = int(input("请输入数学成绩"))
            students_english_score = int(input("请输入英语成绩"))
            students_dict[students_name]={"chinese":students_chinese_score,"math":students_math_score,"english":students_english_score}
        case 2:
            print("当前进入的是修改学生信息系统")
            students_name_genggai=str(input("请输入需要更改的学生姓名"))
            if(students_name_genggai not in students_dict):
                print("当前学生不存在请检查后再进行修改")
                break
            students_chinese_score_genggai = int(input("请输入更改的语文成绩"))
            students_math_score_genggai=int(input("请输入更改的数学成绩"))
            students_english_score_genggai = int(input("请输入更改的英语成绩"))
            students_dict[students_name_genggai] = {"chinese": students_chinese_score_genggai, "math": students_math_score_genggai, "english": students_english_score_genggai}
        case 3:
            print("当前执行的是删除学生信息系统")
            students_name_genggai=str(input("请输入需要删除的学生信息"))
            if(students_name_genggai not in students_dict):
                print("不存在当前学生请检查后再进行操作")
                break
            students_dict.pop(students_name_genggai)
            #del
            print("删除成功")

        case 4:
            print("当前进行的是查询学生信息操作")
            students_name_genggai = str(input("请输入需要更改的学生姓名"))
            if(students_name_genggai not in students_dict):
                print("当前学生不存在")
                break
            math_score=students_dict[students_name_genggai]["math"]
            chinese_score = students_dict[students_name_genggai]["chinese"]
            english_score = students_dict[students_name_genggai]["english"]
            print(f"数学成绩：{math_score}语文成绩：{chinese_score}英语成绩{english_score}")

        case 5:
            if  not  students_dict:
                print("当前列表为空")
                break
            for students_list in students_dict:
                students_message=students_dict[students_list]
                print(f"姓名：{students_list}\t数学成绩：{students_message["math"]}\t语文成绩：{students_message["chinese"]}\t英语成绩：{students_message["english"]}")
        case 6:
            if not students_dict:
                print("当前系统没有学生数据，无法统计！")
            else:
                # 定义要统计的学科列表：(字典里的key, 显示的中文名称)
                subjects = [("chinese", "语文"), ("math", "数学"), ("english", "英语")]

                for sub_key, sub_name in subjects:
                    # 1. 提取当前学科的所有成绩
                    scores = [info[sub_key] for info in students_dict.values()]

                    # 2. 计算最高分、最低分、平均分
                    max_score = max(scores)
                    min_score = min(scores)
                    avg_score = sum(scores) / len(scores)

                    # 3. 查找最高分和最低分的学员
                    max_students = [name for name, info in students_dict.items() if info[sub_key] == max_score]
                    min_students = [name for name, info in students_dict.items() if info[sub_key] == min_score]

                    # 4. 格式化输出结果
                    print(f"\n========== {sub_name}成绩统计 ==========")
                    print(f"最高分：{max_score} 分（学员：{', '.join(max_students)}）")
                    print(f"最低分：{min_score} 分（学员：{', '.join(min_students)}）")
                    print(f"平均分：{avg_score:.2f} 分")

        case 7:
            print("退出系统")
            break