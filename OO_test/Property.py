class person:
    def __init__(self):
        self.__age = 18
        pass

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     if age < 0:
    #         print("年龄小于0")
    #         pass
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    #
    # age = property(get_age, set_age)
    @property
    def age(self):
        return self.__age()

    @age.setter
    def age(self, parms):
        if parms < 0:
            print("年龄小于0")
            pass
        else:
            self.__age = parms
            pass
        pass

    pass


p1 = person()
print(p1.age)
