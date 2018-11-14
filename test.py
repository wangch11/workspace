#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("I\'m learning Python")   #I'm learning Python

print(r"I\'m learning Python")  #I\'m learning Python

print(r'''hello,\n
world''')

print('''hello,
    world''')                   #'''....'''输出多行

print( 5 > 3 and 3 > 1)         #true

print(10//3)                    #3结果为整数
print(9/3)                      #3.0结果为浮点数

print("中文测试")

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

name = ["小明", "小红", "小兰"]
print(name)
name.append("小刚")
print(name)
name.insert(1, "小青")
print(name)
name.pop()
print(name)


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
d.pop('Bob')
print(d)

s = set([1, 1, 2, 2, 3, 3])
print(s)

n1 = 255
n2 = 1000
print(hex(n1), hex(n2))