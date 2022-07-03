import time


class People:
    country = "China"

    @classmethod  # 类方法
    def getCountry(cls):
        return cls.country  # 访问类属性
        pass

    @classmethod
    def changeCountry(cls, data):
        cls.country = data
        pass

    @staticmethod
    def getTime():
        return time.strftime("%H：%H：%S",time.localtime())
        pass


# print(People.getCountry())
# p = People()
# print(p.getCountry())
# People.changeCountry("英国")
# print(People.getCountry())
# print(p.getCountry())
print(People.getTime())