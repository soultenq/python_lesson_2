'''
Задача 7
Найти произведение цифр числа.
'''

stack=[]
integer_number = 21210
mult=1

for i in str(integer_number):
    stack.append(i)
    print(stack)
    if '0' in stack:
        continue
    mult = mult*int(stack.pop())

print(mult)
