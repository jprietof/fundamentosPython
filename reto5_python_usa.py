# reto 5

# Crear un diccionario llave sera el codigo del producto y una lista con el nombre, precio e inventario

accion = input()
val1, val2, val3, val4 = input().split()
code = int(val1)
name = val2
price = float(val3)
cant = int(val4)

productos = {1:["Tangelos", 9000.0, 67],
            2:["Limones", 2500.0, 35],
            3:["Peras", 2700.0, 65],
            4:["Arandanos", 9300.0, 34],
            5:["Tomates", 8100.0, 42],
            6:["Fresas", 9100.0, 90],
            7:["Helado", 4500.0, 41],
            8:["Galletas", 700.0, 18],
            9:["Chocolates", 4500.0, 80],
            10:["Jamon", 11000.0, 55]}



def agregar(codigo, nombre, precio, inventario):
    if codigo not in productos:
        productos[codigo]=[nombre, precio, inventario]
        return True
    else:
        return False

def actualizar(codigo, nombre, precio, inventario):
    if codigo in productos:
        productos[codigo]=[nombre, precio, inventario]
        return True
    else:
        return False

def borrar(codigo):
    if codigo in productos:
        productos.pop(codigo)
        return True
    else:
        return False

def analizarDatos():
    total_precio = 0
    val_invent = 0

    for id in productos:
        total_precio += productos[id][1]
        val_invent += productos[id][1] * productos[id][2]
    
    promedio = total_precio / len(productos)
    valMenor = min(productos, key=lambda k: productos[k][1])
    valMayor = max(productos, key=lambda k: productos[k][1])
    return print(productos[valMayor][0], productos[valMenor][0], round(promedio,1), round(val_invent,1))


if accion == "ACTUALIZAR":
    if actualizar(code, name, price, cant):
        analizarDatos()
    else:
        print("ERROR")

elif accion == "AGREGAR":
    if agregar(code, name, price, cant):
        analizarDatos()
    else:
        print("ERROR")

elif accion == "BORRAR":
    if borrar(code):
        analizarDatos()
    else:
        print("ERROR")