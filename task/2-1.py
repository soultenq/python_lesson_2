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

