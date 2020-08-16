'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

stack=[]
integer_number = 21301

for i in str(integer_number):
    stack.append(i)
    print(stack.pop())
