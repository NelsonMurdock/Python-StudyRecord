class People:
    def __init__(self):
        self.__name = "谭卓杰"  # 私有化，两个下划线
        self.age = "22"
        pass

    #
    #     # def __str__(self):
    #     #     return "{}的年龄是{}".format(self.__name, self.age)
    #
    #


class Student(People):
    def printInfo(self):
        print(self.age)
        pass

    pass


#
#
# p1 = People()
# print(p1.age)
p2 = Student()
p2.printInfo()
print("hhh")
