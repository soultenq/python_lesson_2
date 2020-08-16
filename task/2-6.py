''''
Задача 6
Найти сумму цифр числа.
'''

stack=[]
integer_number = 21301
sum=0

for i in str(integer_number):
    stack.append(i)
    sum = sum + int(stack.pop())

print(sum)