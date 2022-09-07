#       P1   P2   P3   P4
# A1   150   100  80   40
# A2   35    40   120  20
# A3   80    28   40   58
# A4   120   95   20   90
# A5   230   32   31   5


ventas=[[150,100,80,40],[35,40,120,20],[80,28,40,58],[120,95,20,90],[230,32,31,5]]
sumat=[]
for P in range(4):
    sumar=0
    for A in range(5):
        sumar=sumar+ventas[A][P]
    sumat.append(sumar)
for i in range(5):
    print(ventas[i])
print(sumat)    
for i in range(4):
    print('P'+str(i+1),'=>',sumat[i])
#Sumatoria de Almacenes
sumaA=[]
for A in range(5):
    sumar=0
    for P in range(4):
        sumar=sumar+ventas[A][P]
    sumaA.append(sumar)
for i in range(5):
    print('A'+str(i+1),'=>',sumaA[i])