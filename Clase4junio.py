def validarentradas(validar,mensaje):
    while True:
        try:
            if validar=='A': dato=int(input(mensaje))
            elif validar=='B': dato=float(input(mensaje))
            else: dato=input(mensaje)
            break
        except:
            print('Datos Incorrectos')
    return dato
def titulo():
    print('--------------------------')
    print('Capturar Identificaciones')
    print('--------------------------')
def calcularespacios(tamaños):
        resultado=[]
        resultado.append((10-tamaños[0])*' ')
        resultado.append((20-tamaños[1])*' ')
        resultado.append((10-tamaños[2])*' ')
        resultado.append((4-tamaños[3])*' ')
        resultado.append((10-tamaños[4])*' ')
        return resultado




def capturarinfo():
    documentos=[]
    nombre=[]
    telefono=[]
    horastrab=[]
    vrhora=[]
   
    while True:
        titulo()
        cedula=validarentradas('A', 'Ingrese el Documento de identidad ')
        nomb=validarentradas('C', 'Ingrese el Nombre ')
        tel=validarentradas('A', 'Ingrese el Telefono ')
        ht=validarentradas('A', 'Ingrese Hora Trabajadas ')
        vh=validarentradas('B', 'Ingrese el Valor Hora ')
        tam=len(documentos)
        validar=True
        for i in range(tam):
            if documentos[i]==cedula:
                print('Cedula ya Existe')
                validar=False
        if validar==True:
           
            documentos.append(cedula)
            nombre.append(nomb)
            telefono.append(tel)
            horastrab.append(ht)
            vrhora.append(vh)
            print('Informacion Almacenda')
        pregunta=validarentradas('Cualquiercosas','Desea Seguir Ingresnado datos?')
        if pregunta !='s': break
   
    tam=len(documentos)
    total=0
    print('No. Cedula   Nombre                Telefono      Horas    Vr Hora     Total a Pagar')
    vecttam=[0,0,0,0,0]
    for i in range(tam):
        vecttam=[len(str(documentos[i])),len(nombre[i]),len(str(telefono[i])),len(str(horastrab[i])),len(str(vrhora[i]))]
        resultado=calcularespacios(vecttam)    
       
        print(i+1, documentos[i],resultado[0],nombre[i],resultado[1],telefono[i],resultado[2],horastrab[i],resultado[3],vrhora[i],resultado[4],horastrab[i]*vrhora[i])
        total +=horastrab[i]*vrhora[i]
    print('------------------------------------------------------------------')
    print('Total Nomina:', total)
    print('------------------------------------------------------------------')    


capturarinfo()