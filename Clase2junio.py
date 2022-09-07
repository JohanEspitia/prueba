# Solicitar 10 numeros
# opcion # 1 : cuantos +, - , 0
# opcion # 2 : Calcular en un rango pares, impares y ceros.
# opcion # 3 : submenu cadena caracteres convertila a mayusculas, minusculas y contar A, B, C, Otras
from ast import Try
submenu='Menu Cadenas\n1->Ingresar Nombre\n2->Mayusculas\n3->Minusculas\n4->Calculo \n5->Regresar'
menu='Menu Principal\n1->Calculo de Valores\n2->Calcular Pares e Impares\n3->Manipulacion de String\n5->Salir'
def calculonumero():
    positivos=0
    negativos=0
    neutro=0
    for i in range(10):
        numero=int(input('Ingrese un Numero: '))
        if numero>0: positivos +=1
        elif numero<0: negativos +=1
        else: neutro +=1
    print('Positivos: ', positivos)    
    print('Negativos: ', negativos)    
    print('Neutros  : ', neutro)
def paresimpares():
    pares=0
    impares=0
    ceros=0
    for i in range(10):
        numero=int(input('Ingrese un Valor'))
        if numero==0: ceros +=1
        elif numero%2==0:
            print(numero%2)
            pares +=1
        else: impares +=1
    print('Pares  :' , pares)
    print('Impares:', impares)
    print('Ceros  :', ceros)
def calculocadenas(cadenatexto):
    contarA=0
    contarB=0
    contarC=0
    contarO=0
    for i in range(len(cadenatexto)):
        if str.upper(cadenatexto[i])=='A': contarA +=1
        elif str.upper(cadenatexto[i])=='B':contarB +=1
        elif str.upper(cadenatexto[i])=='C':contarC +=1
        elif cadenatexto[i] !=' ': contarO +=1
       
    print('A=>', contarA, 'B=>', contarB, 'C=>', contarC, 'Otros=>', contarO)        
def mayuminus(tipo,texto):
    if tipo=='M': print(str.upper(texto))
    else: print(str.lower(texto))
def validarentradas(tipo,mensaje):
    while True:
        try:
            if tipo=='E': valor=int(input(mensaje))
            else: valor=input(mensaje)
            break
        except:
            print('Error en el tipo de dato')
    return valor
def cadenastexto():
    cadena=''
    while True:
        print(submenu)
        op1=validarentradas('E','Ingrese una opcion :=> ')
        if op1==1:
            cadena=validarentradas('s','Ingrese el Nombre:==> ')
        elif op1==2: mayuminus('M',cadena)
        elif op1==3: mayuminus('m',cadena)
        elif op1==4:
           calculocadenas(cadena)                
        elif op1==5:break    
while True:
    print(menu)
    op=validarentradas('E','Seleccione una Opcion:> ')
    if op==1:
        calculonumero()
       
    elif op==2:
        paresimpares()
    elif op==3:
        cadenastexto()
   
    elif op==5: break