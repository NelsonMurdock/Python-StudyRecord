# def copyfile():
#     old_file = input("请输入要备份的文件名")
#     file_list = old_file.split(".")
#     new_file = file_list[0]+"_备份."+file_list[1]
#     old_f = open(old_file,"r")
#     new_f = open(new_file,"w")
#     content = old_f.read()
#     new_f.write(content)
#     old_f.close()
#     new_f.close()
#     pass
#
# copyfile()

def copyfile():
    old_file = input("请输入要备份的文件名")
    file_list = old_file.split(".")
    new_file = file_list[0] + "_备份." + file_list[1]
    try:
        with open(old_file, "r") as old_f, open(new_file, "w") as new_f:
            while True:
                conent = old_f.read(1024)
                new_f.write(conent)
                if len(conent) < 1024:
                    break
    except Exception as msg:
        print(msg)
    pass


copyfile()
