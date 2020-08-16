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
