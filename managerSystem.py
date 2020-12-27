"""
步骤：
    1.程序入口函数：
        ·加载数据
        ·显示所有功能
        ·用户输入序号
        ·更具序号实现不同功能
    2.系统功能函数
        ·添加/删除/修改/查询/显示所有/保存/退出
    3.储存数据（文件）：
        加载文件数据
        修改数据后保存到文件
"""
from student import *


class StudentManger(object):
    def __init__(self):
        # 储存学员信息的列表
        self.student_list = []

    # 一.程序入口函数
    def run(self):
        # 1.加载学员信息
        self.load_student()

        while True:
            # 2.显示功能菜单
            self.show_menu()

            # 3.输入功能序号
            menu_num = int(input("请输入功能序号："))

            # 4.判断用户输入
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break
            else:
                print("输入错误，请重新输入：")

    # 二.功能函数
    # 2.1显示功能菜单
    def show_menu(self):
        print('------------管理员系统----------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')
        print('-----------管理员系统-----------')

    # 添加学员
    def add_student(self):
        name = input("请输入你的姓名：")
        gender = input("请输入你的性别：")
        password = input("请输入你的密码：")

        # 创建学员对象，将学员添加至列表
        student = Student(name, gender, password)
        self.student_list.append(student)

        # 打印信息
        print(student)

    # 删除学员
    def del_student(self):
        del_name = input("请输入要删除的学员姓名：")

        # 判断是否存在
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('请输入正确的名字')

    # 修改学员信息
    def modify_student(self):
        modify_name = input("请输入要修改的学员姓名：")

        # 判断是否存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input("请输入学员姓名：")
                i.gender = input("请输入学员性别：")
                i.password = input("请输入学员密码：")
                print(f'修改成功，姓名{i.name},性别{i.gender},密码{i.password}')
                break
        else:
            print('请输入正确的名字')


    # 查询学员信息
    def search_student(self):
        search_name = input("请输入要查询的学员姓名：")

        # 判断是否存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'查询成功，姓名{i.name},性别{i.gender},密码{i.password}')
                break
        else:
            print('请输入正确的名字')

        # print(*self.student_list, sep="\n")  输出整个列表，*将列表变为参数，sep表示以这个分割

    # 显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t密码')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.password}')

    # 保存所有学员信息
    def save_student(self):
        f = open('student.data', 'w')

        # 将学生信息写入文件数据
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))

        f.close()

    # 加载学员信息
    def load_student(self):
        # 以r打开数据文件，不存在则以W打开
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据
            data = f.read()

            # 字符串-->字典-->对象
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['password']) for i in new_list]
        finally:
            f.close()
