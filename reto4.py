def restamatriz(a,b):
    c = []
    for i in range (len(a)):
        c.append([0 for i in range(len(a[0]))])
    for k in range (len(a)) :  
        for i in range(len(a[0])):
            c[k][i] = (a[k][i]-b[k][i])
    return c

def menor(num, num1, medmenor) :
    menor = medmenor[num - 1][0]
    posmay = 1
    for i in range (num1):
        if medmenor[num - 1][i] < menor :
            menor = medmenor[num - 1][i]
            posmay = i + 1
               

    print(posmay, menor)

def mayor(num, num1, medmayor):
    mayor = medmayor[num - 1][0]
    posmay = 1
    for i in range (num1):
        if medmayor[num - 1][i] > mayor :
            mayor = medmayor[num - 1][i]
            posmay = i + 1

    print(posmay, mayor)
    
def get_elem_index(a,elem=None):
    if elem=='min':
        return min(a),a.index(min(a))
    elif elem=='max':
        return max(a),a.index(max(a))
    else:
        return elem,a.index(elem)
def get_average(ext_list):
    if len(ext_list)>0:
        return sum(ext_list)/len(ext_list)
    return 0
def get_min_max_avg(existences):
    result=[]
    for exist in existences:
        if len(exist)>0:
            result.append([min(exist),get_average(exist),max(exist)])
        else:
            result.append([0 for i in range(3)])
    return result
def get_avg_per_patient(meds,n_pat):
    if n_pat>0:
        return sum(meds)/n_pat

    return 0

def departminmax(num, listemp):
    a = len(listemp)
    b = len(listemp[0])
    vector1 = []
    if a == 1 and listemp[0][0] == 0 :
        print (1, 0)
        print (1, 0)
    else :
        for i in range (num):
            vector1.append(0)
        for i in range (a) :
            c = listemp[i][0]
            vector1[c - 1] = listemp[i][1]    
        mayor = max(vector1)
        posmayor = vector1.index(mayor) + 1
        menor = min(vector1)
        posmenor = vector1.index(menor) + 1
        print (posmenor, menor)
        print (posmayor, mayor) 


def main():
    n,k = 0,0
    while n<1 or k<1:
        ini_data=input().split(' ')
        n,k,m=int(ini_data[0]),int(ini_data[1]),int(ini_data[2])
    actual_ex,req_ex,bra_count, matriz = [],[],[],[]
    for i in range(n):
        read_ex = list(map(lambda x: int(x), input().split(' ')))
        actual_ex.append(read_ex)
        req_ex.append([0 for i in range(k)])
        bra_count.append(0)
    for i in range(m):
        band = 0
        listsuc = []
        read_info=input().split(' ')
        suk,med_type,n_dosis,s,d=int(read_info[0]),int(read_info[1]), int(read_info[2]), int(read_info[3]), int(read_info[4])
        read_info.pop(4)
        read_info.pop(3)
        if 0<suk<=n and 0<med_type<=k and n_dosis>= 0:
            if s<70 and d<50:
                req_ex[suk-1][med_type-1]+=n_dosis   
            elif 120<=s<130 and 75<=d<80:
                req_ex[suk-1][med_type-1]+=n_dosis   
            elif 130<=s<150 and 80<=d<90:
                req_ex[suk-1][med_type-1]+=n_dosis   
            elif 150<=s<170 and 90<=d<100:
                req_ex[suk-1][med_type-1]+=n_dosis    
            elif s>=170 and d>=100:
                req_ex[suk-1][med_type-1]+=n_dosis   
            elif s>=130 and d<80:
                req_ex[suk-1][med_type-1]+= n_dosis
            else : band = 1   
                
            bra_count[suk-1]+= 1

            if med_type == 1: 
                if band == 1 :
                    continue
                else :
                    listsuc.append(suk)
                    listsuc.append(n_dosis)
                    matriz.append (listsuc)
            else: band = 0         

    if band == 0 : 
        listsuc.append(0)
        listsuc.append(0)
        matriz.append (listsuc)     

    final_ex=restamatriz(actual_ex,req_ex)
    min_max_avg=get_min_max_avg(req_ex)
    
    for i in range (n) :
        print (i + 1)
        menor (i + 1, k, final_ex)
        mayor (i + 1, k, final_ex)
        print(str((f"{min_max_avg[i][0]:.{2}f}")), str((f"{min_max_avg[i][1]:.{2}f}")), str((f"{min_max_avg[i][2]:.{2}f}"))) 
        print(str((f"{get_avg_per_patient (req_ex[i], bra_count[i]):.{2}f}")))
    departminmax(n, matriz)
if __name__ == "__main__":
    main()