def archivosCSV():
    f=open('./bdClientes.csv','r')
    fila=1
    lista=[]
    for item in f:
        dic={}
        if fila==1:
            nombredic=item.rstrip('\n').split('|')
            fila=2
        else:
            linea=item.rstrip('\n').split('|')
            dic[nombredic[0]]=linea[0]
            dic[nombredic[1]]=linea[1]
            dic[nombredic[2]]=linea[2]
            dic[nombredic[3]]=linea[3]
            lista.append(dic)
   
    for i in range(len(lista)):
        print(lista[i])
archivosCSV()