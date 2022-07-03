# class Animal:
#     def __init__(self):
#         self.color = "红色"
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#     #   return object.__new__(cls,*args,**kwargs)
class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
            pass
        return cls._instance


d1 = DataBaseClass()
print(id(d1))
d2 = DataBaseClass()
print(id(d2))
