"""#vectores
n=int(input('Ingrese N: '))
valores=[0,0,0,0]
c=[0,0,0,0]
for i in range(n):
    num=int(input('Ingrese el valor: '))
    valores[i]=num
    c[i]=valores[i]*valores[i]
for j in range(n):
    print('Valor',valores[j],'al cuadrado',c[j])"""
""""
n=int(input('Ingrese N: '))
valores=[]
c=[]
for i in range(n):
    num=int(input('Ingrese el valor: '))
    valores.append(num)
    c.append(valores[i]*valores[i])
for j in range(n):
    print('Valor',valores[j],'al cuadrado',c[j])

"""
edad=[]
def edades():
    while True:
        vedad=int(input('Ingrese la edad'))
        edad.append(vedad)
        continuar=input('Desea Continuar?')
        if continuar !='s': break
def validar():
     tam=len(edad)
     contarM=0
     contarm=0
     for i in range(tam):
         if edad[i]>=18:contarM +=1
         else: contarm +=1
     print('Mayores',contarM,'Menores',contarm)
     edad.clear()  
menup=['1-Capturar Edad', '2-Validar Edad']
def menu():
    for i in menup:
        print(i)
while True:
    menu()
    op=int(input('Seleccione una opcion: '))
    if op==1: edades()
    elif op==2: validar()