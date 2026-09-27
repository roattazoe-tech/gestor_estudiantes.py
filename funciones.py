def crear_estudiante(legajo, nombre, curso):
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "curso": curso,
        "notas": [],
        "materias": []
    }

    print("\nEstudiante creado correctamente:")
    mostrar_diccionario(estudiante)

    return estudiante


def listar_estudiantes(lista):
    if len(lista) == 0:
        print("\nNo hay estudiantes registrados.")
    else:
        print("\n===== LISTA DE ESTUDIANTES =====")

        for estudiante in lista:
            mostrar_diccionario(estudiante)
            print("------------------------------")


def listar_nombres(lista):
    if len(lista) == 0:
        print("\nNo hay estudiantes registrados.")
    else:
        print("\n===== ESTUDIANTES =====")

        for i in range(len(lista)):
            print(f"ID: {i} - Nombre: {lista[i]['nombre']}")


def mostrar_diccionario(dic):
    print("\n===== DATOS DEL ESTUDIANTE =====")
    print("Legajo:", dic["legajo"])
    print("Nombre:", dic["nombre"])
    print("Curso:", dic["curso"])

    if len(dic["notas"]) == 0:
        print("Notas: No tiene notas registradas.")
    else:
        print("Notas:", dic["notas"])

    if len(dic["materias"]) == 0:
        print("Materias: No tiene materias registradas.")
    else:
        print("Materias:", dic["materias"])


def calcularPromedioLista(lista):
    if len(lista) == 0:
        print("El estudiante no tiene notas registradas.")
        return 0

    suma = 0

    for nota in lista:
        suma += nota

    promedio = suma / len(lista)

    return promedio