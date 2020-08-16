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
