test = "TanZhuojie"
# print(type(test))
print("第一个字符:", test[0])
print("第一个字符:%s" % test[0])
print("T" in test)

name = "b aoYi "
print(name)
print("姓名首字母转换大写%s" % name.capitalize())
print("去除字符串两边的空格%s" % name.strip())  # lstrip()删除左边的空格，rstrip()删除右边的空格

print("name的地址%d" % id(name))
age = name
print("age的地址%d" % id(age))

print(name.find("ao"))  # 查找目标对象在序列对象中的位置
print(name.find("e"))  # 没有返回-1
print(name.index("ao"))  # 查找子字符串是否在字符串中，返回下标值
# print(name.index("e"))报错
print(name.startswith("b"))
print(name.lower())
print(name.upper())
print(name[2:5])  # 2-4，还有一个参数默认是1
print(name[:5])  # 从头开始
print(name[2:])  # 最后一个
print(name[2:8])
print(name[::-1])  # 倒序输出，负号表示方向
print(name * 3)
