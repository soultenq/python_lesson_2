'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
stack=[]
dd={}
k=0
r='0'
j=0
m=80

x=0
y=0

while k < m:
    r= ''.join((r,'0'))
    k=k+1

while j < 5:
#   stack.append(r)
    j = j +1
    dd[j]=r

#for i, a in enumerate(stack):
#    print(i + 1, a)

for x, y in dd.items():
  print(x, y)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

i=0
d=0
a=0

stack=[]

while i<10:
    d = input('Please Enter digit:')
    if not d.isdigit():
        print("Input not valid. Please Enter digit")
        continue
    i+=1
    stack.append(d)
    if d == '5':
        a= a + 1
print('           ')
print('Five count is equal: ' + str(a))'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i

print('Sum of digits from 1 to 100 is: ' + str(sum))

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

import math

a=0
b=10

a=math.factorial(b)

print(a)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

stack=[]
integer_number = 21301

for i in str(integer_number):
    stack.append(i)
    print(stack.pop())
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

print(sum)'''
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
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

integer_number = 2134135
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''
Задача 9
Найти максимальную цифру в числе
'''

mvalue=0
integer_number = 291341
while integer_number > 0:
    if mvalue < integer_number % 10:
       mvalue = integer_number % 10
    integer_number = integer_number//10
print(mvalue)
'''
Задача 10
Найти количество цифр 5 в числе
'''
value=0
count=0
integer_number = 291341555
while integer_number > 0:
    value = integer_number % 10
    if value == 5:
        count+=1
    integer_number = integer_number//10
print(count)
