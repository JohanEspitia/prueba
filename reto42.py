n=0
k=0
while n<1 and k<1:
    n,k,m=map(int,input().split())

t_med=0
med=[]
m_med=[],[]
m_suma_med=[],[]
sede=[]
n_sucur=[]
p_sist=[]
p_dist=[]
med_orig=[]
sum_med=[]
suma=0
s=0


#print(n)

for i in range(n):
        medi=0
        sucur=0
        while medi<1:
            medi=int(input())
        med.append(medi)
        n_sucur.append(i+1) 
        med_orig.append(medi)
        m_med=[[n_sucur],[med]]
 

for i in range(m):
        # captura sede y presion
        s,sist,dist=map(int,input().split())
        sede.append(s)
        p_sist.append(sist)
        p_dist.append(dist)

                
      
        if sist < 70 and dist < 50:
            t_med=5
        elif 70 <= sist <= 110 and 50 <= dist <= 70:
            t_med=0
        elif 110 <= sist <= 120 and 70 <= dist <= 75:
            t_med=0
        elif 120 <= sist <= 130 and 75 <= dist <= 80:
            t_med=10
        elif 130 <= sist <= 150 and 80 <= dist <= 90:
            t_med=15
        elif 150 <= sist <= 170 and 90 <= dist <= 100:
            t_med=25
        elif sist >= 170 and dist >= 100:
            t_med=45
        elif sist >= 130 and dist < 80:
            t_med=25
            
            
          
        sum_med.append(t_med)

m_pasi=[[sede],[p_sist],[p_dist]]

m_suma_med=[[sede],[sum_med]]

print(m_pasi)

m_med=[[n_sucur],[med]]
print(m_suma_med)

print(m_med)

#Organiza la lista de medicamentos

med.sort(reverse=True)
med.reverse()

print(med)



#Resultado
print("_______________")
print(med_orig.index(med[-len(med)])+1," ",med[-len(med)]) #imprime el menor inventario de la lista
print(med_orig.index(med[-1])+1," ",med[-1]) #imprime el mayor inventario de la lista


for i in range(n):
  print(i+1)
