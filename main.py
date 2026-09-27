from funciones.gestor_estudiante import (
    crear_estudiante,
    listar_estudiantes,
    listar_nombres,
    mostrar_diccionario,
    calcularPromedioLista
)


lista_bd = []

opcion = ""

while opcion != "7":

    print("\n========== SISTEMA DE GESTION ESCOLAR ==========")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Ingresar nota a un estudiante")
    print("4. Calcular promedio individual")
    print("5. Agregar una materia a un estudiante")
    print("6. Mostrar materias de un estudiante")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    # OPCION 1: Crear estudiante
    if opcion == "1":

        legajo = len(lista_bd) + 1000

        nombre = input("Ingrese el nombre del estudiante: ")
        curso = input("Ingrese el curso: ")

        estudiante = crear_estudiante(legajo, nombre, curso)

        lista_bd.append(estudiante)

    # OPCION 2: Listar estudiantes
    elif opcion == "2":

        listar_estudiantes(lista_bd)

    # OPCION 3: Ingresar una nota
    elif opcion == "3":

        if len(lista_bd) == 0:
            print("No hay estudiantes registrados.")

        else:
            listar_nombres(lista_bd)

            try:
                indice = int(input("Ingrese el ID del estudiante: "))

                if indice >= 0 and indice < len(lista_bd):

                    nota = float(input("Ingrese la nota numerica: "))

                    lista_bd[indice]["notas"].append(nota)

                    print("Nota agregada correctamente.")

                else:
                    print("El ID ingresado no existe.")

            except ValueError:
                print("Debe ingresar un numero valido.")

    # OPCION 4: Calcular promedio
    elif opcion == "4":

        if len(lista_bd) == 0:
            print("No hay estudiantes registrados.")

        else:
            listar_nombres(lista_bd)

            try:
                indice = int(input("Ingrese el ID del estudiante: "))

                if indice >= 0 and indice < len(lista_bd):

                    notas = lista_bd[indice]["notas"]

                    promedio = calcularPromedioLista(notas)

                    print(
                        "El promedio de",
                        lista_bd[indice]["nombre"],
                        "es:",
                        promedio
                    )

                else:
                    print("El ID ingresado no existe.")

            except ValueError:
                print("Debe ingresar un numero valido.")

    # OPCION 5: Agregar una materia
    elif opcion == "5":

        if len(lista_bd) == 0:
            print("No hay estudiantes registrados.")

        else:
            listar_nombres(lista_bd)

            try:
                indice = int(input("Ingrese el ID del estudiante: "))

                if indice >= 0 and indice < len(lista_bd):

                    materia = input("Ingrese el nombre de la materia: ")

                    lista_bd[indice]["materias"].append(materia)

                    print("Materia agregada correctamente.")

                else:
                    print("El ID ingresado no existe.")

            except ValueError:
                print("Debe ingresar un numero valido.")

    # OPCION 6: Mostrar materias
    elif opcion == "6":

        if len(lista_bd) == 0:
            print("No hay estudiantes registrados.")

        else:
            listar_nombres(lista_bd)

            try:
                indice = int(input("Ingrese el ID del estudiante: "))

                if indice >= 0 and indice < len(lista_bd):

                    estudiante = lista_bd[indice]

                    print(
                        "\nMaterias de",
                        estudiante["nombre"],
                        ":"
                    )

                    if len(estudiante["materias"]) == 0:
                        print("El estudiante no tiene materias registradas.")
                    else:
                        for materia in estudiante["materias"]:
                            print("-", materia)

                else:
                    print("El ID ingresado no existe.")

            except ValueError:
                print("Debe ingresar un numero valido.")

    # OPCION 7: Salir
    elif opcion == "7":

        print("Saliendo del sistema...")

    else:
        print("Opcion incorrecta. Intente nuevamente.")