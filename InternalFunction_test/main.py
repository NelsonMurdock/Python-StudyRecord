# print(abs(-1))  # 绝对值
# print(round(3.66, 1))  # 近似值
# print(pow(2, 3))  # 求次方
# print(3 ** 3)
# print(max([23, 22, 4, 5, 8, 9, 10]))
# a, b, c = 1, 2, 3
# print(eval("a+b+c"))  # 执行表达式，也可以执行函数
# li = [2, 45, 66, 99, 8, 4, 10]
# li.sort()  # 只对序列有效
# print(li)

# def printBoookInfo():
#     books = []
#     id = input("请输入编号：每个项以,分隔")
#     bookname = input("请输入书名：每个项以,分隔")
#     bookPos = input("请输入位置：每个项以,分隔")
#     idList = id.split(",")  # 按照,分隔
#     nameList = bookname.split(",")
#     posList = bookPos.split(",")
#
#     bookInfo = zip(idList, nameList, posList)
#     for bookItem in bookInfo:
#         dicInfo = {"编号": bookItem[0], "书名": bookItem[1], "位置": bookItem[2]}
#         books.append(dicInfo)
#         pass
#     for item in books:
#         print(item)
#         pass
#     pass


# printBoookInfo()

# set1 = {1,2,3,4}
# set2 = {3,4,5}
# print(set1-set2)
# rs1 = set1.difference(set2)
# print(rs1)
# print(set1&set2)
# rs2 = set1.intersection(set2)
# print(rs2)
# print(set1 | set2)
# print(set1.union(set2))

li = [1, 3, 4, 3, 3, 5, 2, 4, 2, 5, 2]
set1 = set(li)
print(set1)
for i in set1:
    li.remove(i)  # 删掉一个就退出了
    pass
print(li)
set2 = set(li)
print(set2)
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass
pass
