"""控制台菜单与用户交互，具体的功能如下:
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过
1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
5.展示全部学生成绩:展示出系统中所有学生的成绩"""


#1。添加学生成绩
#2，修改学生成绩
#3.删除学生成绩从
#4.查询学生成绩
#5 展示全部学生的成绩
#学生类

class Students:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"姓名{self.name} | 语文{self.chinese}| 数学{self.math}|英语{self.english} |总分{self.chinese+self.math+self.english}"
    def update_score(self,chinese,math,english): #可以提前给相应的参数设定默认值 如果只修改单个科目成绩的时候就不许要再一个个统计了
        if chinese is not None and math is not None and english is not None:
            self.chinese=chinese
            self.math=math
            self.english=english

class EducationMange:
    system_version = "1.0"
    system_name = "理智涵"
    def __init__(self):
        self.student_list = []
#添加学生成绩
    def add_student(self):
        name= input("请输入要添加的姓名") 
        for s in self.student_list:
            if name == s.name:
                print("该学生已经存在")
                return
        chinese=int(input("请输入语文成绩"))
        math=int(input("请输入数学成绩"))
        english=int(input("请输入英语成绩"))
        #判断学生成绩是否在0-100之间的范围之内
        if chinese >=0 and chinese <=100 and math >=0 and math <=100 and english >=0 and english <=100:
            student=Students(name,chinese,math,english)
            self.student_list.append(student)
            print("添加成功")
        else:
            print("成绩不在0-100之间，添加失败")
#修改学生成绩
    def update_student_score(self):
        name=input("请输入需要修改的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"学生{name}的信息：{s}")
                chinese=int (input("请输入修改后的学生语文成绩"))
                math=int (input("请输入修改后的学生数学成绩"))
                english=int (input("请输入修改后的学生英语成绩"))
                #判断分数是否在规定的范围内
                if chinese >=0 and chinese<=100 and math >=0 and math <=100 and english >=0 and english <=100:
                    s.update_score(chinese,math,english)
                    print("修改成功")
                    print(f"修改之后的成绩{s}")

                else:
                    print("成绩不在0-100之间，修改失败")
                return
        print("未找到该学生修改失败")

#删除学生
    def delete_student(self):
        name=input("请输入需要删除的学生姓名")
        for s in self.student_list:
            if  s.name==name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生删除失败")
#查询学生
    def search_student(self):
        name=input("请输入需要查询的学生信息")
        for s in self.student_list:
            if s.name== name:
                print(s)
                return
        print("没有找到该学生")
#展示全部学生成绩
    def deplay_student(self):
        if  not self.student_list  :
            print("当前没有存储成绩无法输出成绩")    
            return
        for s in self.student_list:
            print(f"姓名：{s.name}语文成绩{s.chinese},数学成绩{s.math},英语成绩{s.english}")
      
#运行系统
    def run (self):
        print(f"欢迎使用学生管理系统,版本号{self.system_version},当前编写者{self.system_name}")
        while True:
            print("""
            #   #   #   #   #   #   #   #   #   #
            1.添加学生成绩
            2.修改学生成绩
            3.删除学生成绩
            4.查询学生成绩
            5.展示全部学生成绩
            #   #   #   #   #   #   #   #   #   #
            """)
            choice=int(input("请输入需要的功能"))
            match choice :
                case 1:
                    self.add_student()
                case 2:
                    self.update_student_score()
                case 3:
                    self.delete_student()
                case 4:
                    self.search_student()
                case 5:
                    self.deplay_student()
                case 6:
                    print("感谢您的使用,再见")
                    break
                case _:
                    print("输入错误")
#创建对象
Mange_student = EducationMange()
#运行程序
Mange_student.run()

