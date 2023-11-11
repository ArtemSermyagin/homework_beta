import logging


# logging.basicConfig(level="INFO", filename="mylog.txt")
# log = logging.getLogger()
# print(log)
# # print()
# # print(log.setLevel('DEBUG'))
# print(log.level)
# print(log.info('Привет'))
# print(log.handlers)

def log(func, filename=None):
    def wrapper():
        if filename != None:
            print("Нет")
        else:
            func()
            print(filename)
    return wrapper



@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)