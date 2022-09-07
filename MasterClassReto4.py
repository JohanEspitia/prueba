# #Bienvenidos a Master Class reto 4
# #1. Manejo de Matricez
#     #1.1 Definición de una matriz
#         #1.1.1 Que son? Para que sirven y en que se diferenciand e una lista?
# #2. Operaciones de Matricez
#     # Maximo y minimo deuna matriz
#     # Maximo y minimo de una fila
#     # Operaciones entre matricez


# # M1 = [[Lista],[Lista],[Lista]]
# # notacion del una matriz NxM
# # 3xM
# # M1 = [[Valor,valor,valor],
# #       [Valor,valor,valor],
# #       [Valor,valor,valor]]

# M1 = [[1,2,3],[4,5,6],[7,8,9]]
# Fila = []
# n = 3
# m = 3

# for i in range(n): 
#     Fila = []
#     for j in range(m):
#         valor = int(input())
#         Fila.append(valor)
#     M1.append(Fila)

# #Minimo
# Minimos = 10000
# for i in range(n):
#     fila = min(M1[i])
#     if fila < Minimos:
#         Minimos = fila

# print('Minimo', Minimos)
# #Maximo
# Maximo = -99999
# for i in range(n):
#     fila = max(M1[i])

#     if fila > Maximo:
#         Maximo = fila
#         fila = i

# print('Maximo', Maximo)
# #Imprimir indice
# indice = M1[i].index(Maximo)
# print(i, ',', indice)

# #Suma de filas
# for i in range(n):
#     print(sum(M1[i]))

# #llamar un elemento dentro de una matrix
# Columna = []
# for elemento in M1:
#     print(elemento)
#     Columna.append(elemento[0])
#     #print la primera columna
#     #print(elemento[0])

# #2da notacion:
# Columna = [elemento[0] for elemento in M1]
# print(Columna)



# M1 = [[1,2,3],[4,5,6],[7,8,9]]
# M2 = [[1,2,3],[4,5,6],[7,8,9]]






#Los indicies de una matriz
# M1 1,3
# M1[1][3] += -= /=
# M1[1]
#print(M1)

#RETO 4 DE RESCATE, TO DO:
# 1. El sistema debe recibir como entrada la cantidad de sucursales (n) para la entrega de medicamentos
# 1.1 Recibir un variable K que me representa la cantidad de tipos de medicamentos
# 2. Cantidad total de pacientes a atender (m)
# 3. Si la cantidad de sucursales o k es menor a 1 se debe leer nuevamente ambos valores hasta que se ingrese un n válido. 
# 4. se debe leer la cantidad de existencias actuales de todos los tipos de medicamentos en una línea.
# 5. Finalmente, para los m pacientes se debe leer el número de la sucursal donde será atendido, seguido del tipo de medicamento solicitado y el número de existencias solicitadas del mismo,
#  seguido de la información de las presiones sistólica y diastólica


#DUDA:
#1. Como relaciono una sucursal con los tipos de medicamentos
    #1.1 Como hago para asignarle todos los medicamentos a una sucursal
#2. Donde guardo las listas? Matricez?
#3. Existencias programadas? Que es? y que relacion tiene con el programada?
#4. Pacientes por sucursal? Como lo hago?

# Reto 3 -> Lista de medicamentos -> posciones -> Las sucursales
# Reto 4 -> Lista de medicamentos -> por cada sucursal -> Llena medicamentos

# Tengo crear diferentes listas?
# Lista de Medicamentos -> Cambia de Relacion -> las posiciones -> Tipos de medicamento

#Conclusion:
#1. Tengo que crear difenetes lista
#2. Necesito contador? -> Puedo crea una lista de contadores?

#Para arrojar las salidad necesitamos las siguientes:
    # Necesitamos un para que vaya n
    # Necesitamos hacer un print(i+1)
    # Necesitamos hallar el minimo de la fila i y su indice  (Matriz_existencias)(Remitirse arriba)
    # Necesitamos hallar el maximo de la fila i y su indice (Matriz_existencias)(Remitirse arriba)
    # minimo,promedio,maximo de los k tipos de medicamento (Matriz_solicitados)
    # promedio/pacientes

#Sacar el minimo de la primera columna y su indices(Remitirse arriba) (Solicitados)
#Sacar el maximo de la primera columna y su indice(Remitirse arriba)    (Solicitados)

#Solicitdados -> medicamentos solicitados para un tipo de medicamento en un respectiva sucursal

n=0
k=0
m=0
#Pedir sucursal n y m
while n < 1 or k < 1:
    valores_iniciales = input()
    mis_lista_de_variables = valores_iniciales.split()
    n = int(mis_lista_de_variables[0])
    k = int(mis_lista_de_variables[1])
    m = int(mis_lista_de_variables[2])

#Pedir medicamentos hasta que ya no hayan tipos de medicamentos
Lista_medicamentos = []
#K=M
#NxK
Matrix_existencia=[]
for i in range(n):
    #Lista_medicamentos = []
    #for j in range(k):
    #    medicamentos = input().split(' ')
    Lista_medicamentos = input().split(' ')
        #Lista_medicamentos = [Existencia_Med1,  Existencia_Med2, Existencia_Med3, ...,Existencia_Medk]
        #Esto es para una sola sucursal
        #Donde guardo esta información?
        #Podria guardarla en un matriz
    Lista_medicamentos = list(map(int, Lista_medicamentos))
    #map(funcion,Lista)
    #list()
    Matrix_existencia.append(Lista_medicamentos)

print(Matrix_existencia)

#Crear aqui una matrix de ceros(Solicitados):


#Crear una lista de contadores para los pacientes
    #Crear un para un para hasta n
        #hacer .append(0)  a la lista

#Para lo m pacientes
for i in range(m):
    paciente_info = input().split(' ')
    sucursal = int(paciente_info[0]) # Sucursal + 1 / El usuario no sabe que las sucursales empiezan 0
    tipo_med = int(paciente_info[1]) # Tipo_med + 1
    n_dosis = int(paciente_info[2]) #Restar de mi matriz
    sis = int(paciente_info[3])
    dia = int(paciente_info[4])

    if 0 < sucursal <= n and 0 < tipo_med <= k and n_dosis > 0:
        if sis < 91 and dia < 63:
            Matrix_existencia[sucursal-1][tipo_med-1] -= n_dosis
            #Matrix solicitados
            Matrix_solicitados[sucursal-1][tipo_med-1] += n_dosis
            #En que lugar lo resto?
            #Cuales son las posiciones?
            #Como esta la relación de mi matrix_existencias
            #rta: Sucursales son las filas y los tipos de medicamentos las columnas
        elif 162 <= sis < 188 and 105 <= dia < 119:
            Matrix_existencia[sucursal-1][tipo_med - 1] -= n_dosis

        elif 188 <= sis < 201 and 119 <= dia < 126:
            Matrix_existencia[sucursal-1][tipo_med - 1] -= n_dosis
        elif 201 <= sis < 214 and 126 <= dia < 146:
            Matrix_existencia[sucursal-1][tipo_med - 1] -= n_dosis
        elif sis >= 214 and dia >= 146:
            Matrix_existencia[sucursal-1][tipo_med - 1] -= n_dosis
        elif sis >= 152 and dia < 79:
            Matrix_existencia[sucursal-1][tipo_med - 1] -= n_dosis

        #La suma al contador de pacientes
            #Paciente[Sucursal-1] -> Le van a sumar 1