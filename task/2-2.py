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
print('Five count is equal: ' + str(a))