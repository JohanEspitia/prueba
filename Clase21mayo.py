nombre='alex'
print(str.upper(nombre))
nombre='ALEX'
print(str.lower(nombre))
nombre='ALEX'
print(str.capitalize(nombre))
nombre='ALEX vacca'
print(str.count(str.upper(nombre),'A'))
nombre="alex,vacca,ascanio"
print(str.isnumeric(nombre))
print(str.isdecimal(nombre))
separado=str.split(nombre,',')
print(separado[2])