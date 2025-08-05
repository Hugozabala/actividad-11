def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = estudiantes[carnet]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


estudiantes = {}
cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")
    carnet = input("Ingrese el número de carnet: ")
    nombre = input("Ingrese el nombre completo: ")
    edad = int(input("Ingrese la edad: "))
    carrera = input("Ingrese la carrera: ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el número de teléfono: ")

    estudiantes[carnet] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "contacto": {
            "correo": correo,
            "telefono": telefono
        }
    }
a=estudiantes['carnet']={}
resultado = quick_sort(a)
print(resultado)
print("\nLista de estudiantes registrados:")
for carnet, datos in estudiantes.items():
    print(f"\nCarnet: {carnet}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Carrera: {datos['carrera']}")
    print(f"Correo: {datos['contacto']['correo']}")
    print(f"Teléfono: {datos['contacto']['telefono']}")

print("\nBúsqueda de estudiante")
buscado = input("Ingrese el número de carnet que desea buscar: ")

if buscado in estudiantes:
    estudiante = estudiantes[buscado]
    print("\nEstudiante encontrado:")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Carrera: {estudiante['carrera']}")
    print(f"Correo: {estudiante['contacto']['correo']}")
    print(f"Teléfono: {estudiante['contacto']['telefono']}")
else:
    print("Estudiante no encontrado.")

