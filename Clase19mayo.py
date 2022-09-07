
"""
paquete de comentarios de codigo
Nombre, las notas
definiiva=n1*0.3+n2*0.3+n3*0.4
restriccion de notas validas entre 0 y 5
si la note es menor de 3 - reprobado
si la nota esta entre 3 y 3.5 - aprobo bajo
si la nota es 3.5 y 4.5 - aprovado alto
si superior>4.5 - superior
visualizar al final todos los datos el resultado
"""
import math as m #libreria
nombre=input('digite su nombre')
n1=float(input('Ingrese primera nota  '))
n2=float(input('Ingrese segunda nota  '))
n3=float(input('Ingrese tercera nota  '))

print('hola   ',nombre)
if 0<=n1<=5 and 0<=n2<=5 and 0<=n3<=5:
    de=n1*0.3+n2*0.3+n3*0.4
    if de<3:
        print('esta reprobado, su nota es:   ',de)
    elif de<=3.5:
        print('esta aprobado bajo, su nota es:   ',de)
    elif de<=5:
        print('aprobado alto, su nota es  ',de)
else:
    print('introduzca una valor entre 0 y 5')
