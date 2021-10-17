# -*- coding: UTF-8 -*-
# coding=utf-8

'''www'''
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

print("{:,}".format(1000000000))
print('{:#>10d}'.format(11))

print ("{} 对应的位置是 {{0}}".format("runoob"))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

name = 'Runoob'
print(f"Hello {name}")

x=1
print(f'{x+1=}')

print("aKsP".swapcase())