def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
nombre=[]
op=int(input("ingrese cuantos nombres desea ingresar"))
for i in range(op):
    nom=input(("ingree nombre completo"))
    nombre.append(nom)

resultado = quick_sort(nombre)
print(resultado)

