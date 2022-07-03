score = input("请输入你的成绩：")
score = int(score)
if score >= 70:
    print("你及格了！", end="")  # 不换行
    # pass  # 空语句，跳过
    print("123")
elif 60 <= score < 80:
    print("不错")

else:
    print("进厂吧！")
print("结束")

index = 95
while index <= 100:
    print(index)
    index += 1

tag = "谭卓杰大帅比"
for item in tag:
    print(item, end="")
    pass
print("\n")

print(type(range(1, 5)))  # 生成一个数据集合列表，range(起始值,步长），步长不能为0,1-4不包含右边
for data in range(1, 5):
    print(data, end="")
