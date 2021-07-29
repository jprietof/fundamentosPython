val1, val2, val3 = input().split()
distancia = float(val1)
record = float(val2)
tiempo = float(val3)
if distancia > 0 and record > 0 and tiempo > 0:
    valMedio = (distancia*0.001)/(tiempo/3600)
    rPromedio = record + (record *(25/100))
    if valMedio > record and valMedio < rPromedio:
        print("NUEVO RECORD")
    elif valMedio > record and valMedio > rPromedio:
        print("ENTREVISTA")
    else:
        print("VELOCIDAD NORMAL")
else:
    print("VALORES NEGATIVOS")
