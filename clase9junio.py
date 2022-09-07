#1 2 3
#4 5 6
#7 8 9
#1 2 3
#1 2 3
#1 2 3
"""A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[1,2,3],[1,2,3]]
C=[]
filas=[]
for i in range(3):
    print(A[i])
#C=A+B
for f in range(3):                        # 0               0              0          1       1         1
    filas=[]                      
    for c in range(3):                    # 0               1              2          0       1         2
        filas.append(A[f][c]+B[f][c])     # filas=[2]     =[2, 4]      =[2,4,6]     =[5]     =[5,7]    =[5,7,9]
    C.append(filas)                       # C=[[2,4,6]]  C=[[2,4,6],[5,7,9]]  
print(C)
for i in range(3):
    print(C[i])"""

m=[]
fila=[]
for i in range(4):
    fila=[]
    for j in range(4):
         if i==j:
            fila.append(1)
         else:
            fila.append(0)  
    m.append(fila)
for i in range(4):
    print(m[i]) 