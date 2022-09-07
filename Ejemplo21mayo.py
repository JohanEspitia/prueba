plato1='1-> Pizza Hawaina'
plato2='2-> Pizza 3 Quesos'
plato3='3-> Pizza Mexicana'
ing1='Queso, Piña, Jamon'
ing2='Queso1, Queso2, Queso3'
ing3='Queso, Carne Molida, Aji, Guacaomole'
valor1=10000
valor2=12000
valor3=15000
cantidad=int
print('----------------------------')
print(plato1)
print(plato2)
print(plato3)
print('----------------------------')
selplato=int(input('Seleccione la Pizza: '))
ordenfinal='Plato: '
verificar=False
if selplato>0 and selplato<=3:
    verificar=True
    if selplato==1:
        ordenfinal=ordenfinal+plato1 + ' Ingredientes: '+ ing1 +' Valor plato:' + str(valor1)  
        print('Ingrediente:',ing1)
        valor=valor1
    elif selplato==2:
        ordenfinal=ordenfinal+plato2 + ' Ingredientes: '+ing2 +' Valor plato:' + str(valor2)            
        print('Ingrediente:',ing2)
        valor=valor2
    elif selplato==3:
        ordenfinal=ordenfinal+plato3 + ' Ingredientes: '+ing3 +' Valor plato:' + str(valor3)    
        print('Ingrediente:',ing3)
        valor=valor3
else:
    print('Digite una Opcion valida')    
if verificar==True:
    pedido=input('Desea Realizar el Pedido?:')
    pedido=str.upper(pedido)
    if pedido=='SI': 
        cantidad=int(input('cuantas desea llevar?'))
        print(ordenfinal + '  Total:1 ' + str(valor*cantidad))
    else: print('Muchas Gracias, Lo Esperamos Pronto')