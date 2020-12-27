"""
连接student.data
    1.验证姓名，密码是否正确
    2.没有则进行注册
"""
from managerSystem import StudentManger


class StudentRegister(StudentManger):
    stu = StudentManger()
    stu.__init__()
    stu.load_student()

    while True:
        print("--------学生系统-----------")
        print('1:登录')
        print('2:注册')
        print('3:退出')
        print("--------学生系统-----------")

        num = int(input("请输入功能序号："))

        if num == 1:
            stu.load_student()
            stu_name = input("请输入你的姓名：")
            stu_password = input("请输入你的密码：")

            for i in stu.student_list:
                if stu_name == i.name and stu_password == i.password:
                    print(f'登录成功，姓名{i.name},性别{i.gender},密码{i.password}')
                    break
            else:
                print('登陆失败，请检查是否输入正确')

        elif num == 2:
            stu.add_student()
            stu.save_student()
        elif num == 3:
            break
        else:
            print('输入错误，请重新输入')