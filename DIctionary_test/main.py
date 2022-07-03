dic = {}
print(type(dic))
dic["name"] = "tzj"
dic["age"] = 22
print(dic)
print("name" in dic)
print("tzj" in dic)
print(dic["name"])
dic1 = {"pro": "信息", "学校": "武汉理工大学"}
print(dic1, len(dic1))
print("-----------------修改--------------")
dic["name"] = "by"
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
for item in dic.items():
    print(item)
dic.update({"sex": "男"})
print(dic)
print("------------排序----------------------")
print(sorted(dic.items(), key=lambda d: d[0]))  # 0是key，1是value
# print(sorted(dic.items(),key=lambda d: d[1]))这个需要注意value格式
print("--------------删除----------------")
dic.pop("sex")
del dic["age"]
print(dic)
