val1, val2 = input().split()
n=int(val1)
k=int(val2)
numeros = input()
examen = list(map(int, numeros.split(" ")))
contProfe = 0
repetidoPC = []
valor=0
number=0
for num in examen:
    if num in examen[:valor]:
        repetidoPC.append(num)
    if k<n and k==valor:
        if num in examen[number:k]:
            contProfe+=1
            k+=1
            number+=1
        else:
            k+=1
            number+=1
    elif valor < k:
        if num in examen[:valor]:
            contProfe+=1
    valor+=1
print(len(repetidoPC),contProfe)
