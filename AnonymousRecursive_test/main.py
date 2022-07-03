def sum(x, y):
    return x + y


M = lambda x, y: x + y  # 匿名函数

print(sum(1, 2), M(1, 2))

age = 15
print("可以参军" if age > 18 else "继续参军")  # 双分支结构

func = lambda x, y: x if x > y else y
print(func(2, 3))

fun = (lambda x, y: x if x > y else y)(2, 3)
print(fun)


def factorial(n):
    result = 1
    for items in range(1, n + 1):
        result *= items
        pass
    return result


print(factorial(5))


def RecursiveFactorial(n):
    if n == 1:
        return 1
    else:
        return n * RecursiveFactorial(n - 1)


print(RecursiveFactorial(5))
# 模拟实现 树形结构的遍历
import os  # 引入文件操作模块


def findFile(file_path):
    listRs = os.listdir(file_path)  # 得到该路径下所有文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path, fileItem)  # 获取完整文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            findFile(full_path)  # 如果是，再去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass


findFile("D:\\签约")
