num = input()
mensaje = []
for numero in range(int(num)):
    val1, val2, val3, val4, val5 = input().split()
    chasis=int(val1)
    altura=int(val2)
    peso=int(val3)
    cilindraje=int(val4)
    valor=int(val5)
    if chasis <= 2005 and altura <=950 and peso >= 702 and cilindraje <= 1600:
        mensaje.append(valor)

if len(mensaje)==0:
    print("NO DISPONIBLE")
else:
    for n in mensaje:
        print(n)
