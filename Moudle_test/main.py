import os
# from time import ctime, time
#
# print(ctime(), "\n", time)
basePath = "d:/"
for entry in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath,entry)):
        print(entry)
        pass
