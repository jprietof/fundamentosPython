salBase, hExtra, bono = input().split()
salud=4.5
pension=4.5
caja=3
parafiscales = salud + pension + caja

valHora = float(salBase)/186
valExtra = (valHora * 135)/100
valBono = (float(salBase)*5.5)/100
salAntes = float(salBase) + (int(hExtra)*valExtra) + (int(bono)* valBono)
salDespues = salAntes - ((salAntes*parafiscales)/100)
print(round(float(salAntes),1), round(float(salDespues),1))
