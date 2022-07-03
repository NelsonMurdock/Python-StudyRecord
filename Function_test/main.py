pro = "hhhhhhh"  # 全局变量
print(pro)


def printInfo(name, age):
    print("%s大帅比,年龄%d" % (name, age))
    pass


def getComputer(*args):  # 可变长参数
    result = 0
    for item in args:
        result += item
    print(result)
    pass


def keyFunc(**kwargs):
    print(type(kwargs))
    print(kwargs)
    pass


def complexFunc(*args, **kwargs):  # 可选参数必须放到关键字参数之前
    print(args)
    print(kwargs)


def Sum(a, b):
    sum = a + b
    global pro
    pro = "1111"  # 修改全局变量要用到global关键字
    print(pro)
    return sum


def dicFunction(dicA):
    result = {}
    for key, value in dicA.items():  # 函数：包含key，value
        if len(value) > 2:
            result[key] = value[:2]
            pass
        else:
            result[key] = value
            pass
        pass
    return result


Sum(5, 5)

getComputer(1, 2, 3, 4)

dic = {"name": "tzj", "age": "12"}
keyFunc(**dic)
keyFunc(name="tzj", age="12")
keyFunc()
# keyFunc(1,2,3)错误的

complexFunc(1, 2, 3, 4, name="tzj")
complexFunc(age=36)

name = input("请输入姓名：")
age = int(input("请输入年龄："))
printInfo(name, age)
