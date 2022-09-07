#iteraciones y esctructura repetitivas
"""tabla=int(input('ingrese el numero :   '))
i=1 
while i<=10:
    print(tabla, 'x' , i, '=',tabla*i)
    i+=1
i=1
while i<=10:
    print(f"{tabla} x {i} = {tabla*i}")
    i+=1
"""
tabla=int(input('Ingrese el Numero:'))
i=1
while tabla >10 or tabla<=0:
    print('ingrese un valor entre 1 y 10')
    tabla=int(input('Ingrese el Numero:'))
    
print('-------------------')

while i<=10:
    print(f"{tabla} x {i} = {tabla*i}")
    i=i+1