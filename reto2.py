from math import ceil

area_1=8400

area_A=33600
area_B=48900
area_C=17000
area_D=21000
area_E=42600

antea=0
anteb=0
antec=0
anted=0
antee=0

zonas=int(input())
i=0
while i<zonas:
    i=i+1
    area_zona=float(input())
    cantidad=int(input())
    tipo=str(input())
    if cantidad>0:
      if tipo == "a":
        antea += max(0,ceil((area_zona-area_1*cantidad)/33600))
      elif tipo == "b":
        anteb += max(0,ceil((area_zona-area_1*cantidad)/48900))
      elif tipo == "c":
        antec += max(0,ceil((area_zona-area_1*cantidad)/17000))
      elif tipo == "d":
        anted += max(0,ceil((area_zona-area_1*cantidad)/21000))
      elif tipo == "e":
        antee += max(0,ceil((area_zona-area_1*cantidad)/42600))

ante_total = ceil(antea + anteb + antec + anted + antee)

if ante_total>0:
   print(ante_total)
   print("a" , "{:.2f}%". format (antea/ante_total*100))
   print("b" , "{:.2f}%". format (anteb/ante_total*100))
   print("c" , "{:.2f}%". format (antec/ante_total*100))
   print("d" , "{:.2f}%". format (anted/ante_total*100))
   print("e" , "{:.2f}%". format (antee/ante_total*100))
  

else:
  print(ante_total)
  print("a" , "0.00%")
  print("b" , "0.00%")
  print("c" , "0.00%")
  print("d" , "0.00%")
  print("e" , "0.00%")