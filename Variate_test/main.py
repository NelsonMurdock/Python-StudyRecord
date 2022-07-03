a = 10
print(a)
print(type(a))  # type，输出变量类型
b = ()  # 元组类型
print(type(b))
c = []  # 类表类型
print(type(c))
d = {}  # 字典类型
print(type(d))
e = ''  # 数组类型
print(type(e))

f, g, h = 10, 9, 8
print(f, g)
print(f == g)
print(f + g > h and f - g > h)
print(f + g > h or f - g > h)
print(not f - g > h)  # 取反，not x
print(2 > 1 and 1 < 4 or 2 < 3 and 9 < 6 or 2 < 4 and 3 < 2)  # 优先级：（）>not>and>or,然后从左往右
