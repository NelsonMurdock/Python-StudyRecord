import re

# data = "data"
# result = re.match("d", data) # 匹配以“d”为开头
# # print(type(result))
# # print(result.group())

data = "na9999"
res = re.match("[a-z]?", data)
print(res.group())

# d = "a", "b", "c"
# print(type(d))

# res = re.match("[A-Z][a-z]*", "Anyfsfsf")
# print(res.group())
#
# # print(re.match("c:\\\\a.txt","c:\\a.txt").group())
# print(re.match(r"c:\\a.txt","c:\\a.txt").group())

# print(re.match(".*<>","<>sadasdsadsa<>").group())

# res = re.compile("\d{4}")
# print(res.match("12356").group())
#
# rs = re.search("ab","asdbabdsd")
# print(rs.group())
#
# rr = re.findall(r".*", "花S花是sdsda")
# print(rr)
