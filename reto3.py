sut=[]
def sucursales(nums):
    su=[]
    for i in range(nums):
        su.append(int(input()))
    return su

def pacientes(nump):
    pav=[]
    disv=[]
    sisv=[]
    for i in range(nump):
      pa,sis,dis=map(int,input().split())
      pav.append(pa)
      sisv.append(sis)
      disv.append(dis)
    return pav,disv,sisv

su2=[]
while True:
    suc,pac=map(int,input().split())
    if suc>0 and pac>0:
        break
    else: print('Datos erroneos')

su=sucursales(suc)
for u in range(len(su)):
    sut.append(su[u])
pa,dis,sis=pacientes(pac)

for i in range(pac):
    o=pa[i]-1
    l=su[o]
    if sis[i] < 70 and dis[i] < 50:
        l-=5
        su[o]=l
    elif 120 <= sis[i] < 130 and 75 <= dis[i] < 80:
        l-=10
        su[o]=l
    elif 130 <= sis[i] < 150 and 80 <= dis[i] < 90:
        l-=15
        su[o]=l
    elif 150 <= sis[i] < 170 and 90 <= dis[i] < 100:
        l-=25
        su[o]=l
    elif sis[i] >= 170 and dis[i] >= 100:
        l-=45
        su[o]=l
    elif sis[i] >= 130 and dis[i] < 80:
        l-=25
        su[o]=l

may=su[0]
posm=1
for j in range(len(su)):
        if su[j]>may:
            may=su[j]
            posm=j+1

men=su[0]
posme=1
for k in range(len(su)):
        if su[k]<men:
            men=su[k]
            posme=k+1


print(posme, men)
print(posm, may)
for l in range(len(su)):
    print('{:} {:.2f}%'.format(l+1,( 1-( su[l] / sut[l])) * 100))
