ventas=[[100,88,92,94,85,110,118],[30,42,31,32,38,40,37],[23,35,39,45,55,60,61],[45,50,56,65,47,57,68],[18,25,33,21,22,28,32]]
prec=[1500,5000,6500,2500,22500]
for i in range(len(ventas)):
    print(ventas[i])
valores=[]
print(len(ventas))
print(len(ventas[0]))
filaprov=[]
for f in range(len(ventas)):
    filaprov=[]
    for c in range(len(ventas[i])):
        filaprov.append(ventas[f][c]*prec[f])
   
    valores.append(filaprov)
# funcion para calcular el nombre del producto
def buscarprod(indice,proce):
    if proce=='P':
       nombres=['1-> Arroz','2->Papa','3->Yuca','4->Queso','5->Carne']
    else:
       nombres=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    return nombres[indice]    
# Calculo para producto con mas ventas
totalpro=[]
sumaprod=0
for f in range(len(valores)):
    sumaprod=0
    for c in range(len(valores[f])):
        sumaprod += valores[f][c]
   
    totalpro.append(sumaprod)
print(totalpro)
print(buscarprod(totalpro.index(max(totalpro)),'P'),max(totalpro))
print('--------------------------------------')
for i in range(len(totalpro)):
    print(buscarprod(i,'P'),totalpro[i])


for i in range(len(valores)):
    print(valores[i])
#Calcular los dias de la semana y cual es el de mayor venta


valoresDia=[]
sumaDia=0
for c in range(len(valores[0])):
    sumaDia=0
    for f in range(len(valores)):
        sumaDia += valores[f][c]
    valoresDia.append(sumaDia)
print(valoresDia)
print(buscarprod(valoresDia.index(max(valoresDia)),'D'),max(valoresDia))
print('--------------------------------------')
for i in range(len(valoresDia)):
    print(buscarprod(i,'D'),valoresDia[i])
