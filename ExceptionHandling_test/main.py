# try:
#     # print(b)
#     li = [1, 2, 2]
#     print(li[10])
#     pass
# # except NameError as msg:
# #     print(msg)
# #     pass
# # except IndexError as msg:
# #     print(msg)
# except Exception as result:  # Exception捕获所有的异常
#     print(result)
class tooLong(Exception):
    def __init__(self, len):
        self.len = len
        pass

    def __str__(self):
        return "你输入的长度" + str(self.len) + "超过了"

    pass


def name():
    name1 = input("请输入姓名 ")
    try:
        if len(name1) > 5:
            raise tooLong(len(name1))
        else:
            print(name1)
            pass
        pass
    except tooLong as result:
        print(result)
        pass
    finally:
        print("执行完毕")


name()
b = "sdsa"
a = 20
print(a,"sdssds"+b)