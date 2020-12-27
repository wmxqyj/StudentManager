"""
学员信息：姓名、性别、手机号
用___str__返回学员对象信息
"""


class Student(object):
    def __init__(self, name, gender, password):
        self.name = name
        self.gender = gender
        self.password = password

    def __str__(self):
        return f'{self.name},{self.gender},{self.password}'
