import math

antp=8400
a=33600
b=48900
c=17000
d=21000
e=42600

area=float(input())
antint=int(input())
tipoant=input()

areare=area-(antint*antp)

if tipoant=='a':
    re=math.ceil(areare/a)
elif tipoant=='b':
    re=math.ceil(areare/b)
elif tipoant=='c':
    re=math.ceil(areare/c)
elif tipoant=='d':
    re=math.ceil(areare/d)
elif tipoant=='e':
    re=math.ceil(areare/e)

if antint>=0:
    print(re)
    print(areare)
    print(areare/e)
else:
    print('error en los datos')