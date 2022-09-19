
#Version:JA

#End Version:JA

#Version:FR --- Ex-1
def conc(x):
    tP=[]
    tI=[]
    for i in  range(2,x+2,2):
        if (i<x):
            tP.append(i)
    for i in range(1,x+1,2):
        if (i<x):
            tI.append(i)
    if (x%2==0):
        tP.append(x)
        return tP + tI
    else:
        tI.append(x)
        return tI + tP
#End Version:FR Ex-1
#Version:FR --- Ex-3
def identificarCandidatosAMeseta(nums):
    i=0
    candidatos = []
    while(i<len(nums)):
        x=nums[i]
        ci=i
        cf=i
        j=i+1        
        while(j<(len(nums)-1) and nums[i]==nums[j]):
            cf=j
            j+=1
        if (ci!=cf):
            info = [x,ci,cf,cf-ci+1]
            candidatos.append(info)
            i= cf
        i+=1
    return candidatos
#End Version:FR-Ex3

def main():
    #args = get_args()
    print("Hello ¯\_(ツ)_/¯")
    numero_n = int (input("ingresa el numero_Ejercicio-1: "))
    #print(conc(numero_n)) #Call version JA
    print(conc(numero_n))
    numero_n_3 = int (input("ingresa el numero_Ejercicio-3: "))
    nums=[]
    i=1
    while(i<=numero_n_3):
        j=int(input("Ingresa el numero en la posicion " + str(i) + " :"))
        nums.append(j)
        i+=1
    #solo para pruebas, borrar antes de pasarlo
    #nums= [7,2,2,4,5,3,3,3,3,4,2,3,3,2,2]
    candidatos = identificarCandidatosAMeseta(nums) #[[NumeroQueSeRepite,Pos-i,Pos-f,LongitudMeseta],...]
    candidatos_filtro = []
    for i in candidatos:
        if (i[0]>nums[i[1]-1] and i[0]>nums[i[2]+1]):
            candidatos_filtro.append(i)
    if (len(candidatos_filtro)==0):
        print("L:0,P:-1")
    L = 0
    for i in candidatos_filtro:
        if (i[3]>L):
            L= i[3]
    for i in candidatos_filtro:
        if (i[3]>=L):
            print("L:" + str(i[3]) + ",P:" + str(i[1]) + ",N:" + str(i[0]))
            break
    print("À bien tôt \,,/,(><),\,,/")

if __name__ == '__main__':
    main()
