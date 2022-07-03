_list = [1, 2.5, "hello", True]

print(type(_list))
print(len(_list))
print(12 in _list)
print(_list[0:2])
print(_list[1:])
print(_list[::-1])
print(_list * 3)
print("-----------------增加----------------")
_list.append(["123", "222"])
print(_list)
_list.append(88)
print(_list)
_list.insert(1, "44")
print(_list)
rsdata = list(range(10))
_list.extend(rsdata)
_list.extend(["14"])
print(_list)
print("------------删除---------------")
del _list[0]  # 删除第一个
print(_list)
del _list[0:4]  # 批量删除
print(_list)
_list.remove(0)  # 移除指定元素
print(_list)
_list.pop(0)  # 移除第一项元素
print(_list)
print("------------查找--------------")
print(_list.index(88))
print(_list.index(88,0,5))#从0-4查找元素，没有就报异常