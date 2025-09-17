from random import random
for i in range(10):
    a = random()
    if a > 6 or a < 2:
        print(a)
    else:
        print("no")
index = 1
while index <= 10:
    a = random()
    if a<0.2:
        print(a)
    elif 0.2 < a < 0.5:
        print("no")
    else:
        print("a")
    index += 1
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(3,7): # 左闭右开 优化range(len())
    print(list1[i])
str1 = "hello"
for i in range(len(str1)):
    print(i, str1[i])
str1 = "apple"
for i in str1:
    print(i)

def test():
    print("hello world")

# if __name == ‘__main__’:
# 用来防止其他程序调用本程序时，运行本程序的主方法
if __name__ == "__main__":
    test()

