# Programa 1: Programación Tradicional
# Gestión de mascotas usando funciones y variables, sin clases ni objetos.

def registrar_mascota():
    # Solicita los datos de la mascota por teclado
    print("------ Registro de mascota ------")
    nombre = input("Ingrese el nombre: ")
    especie = input("Ingrese la especie: ")

    # Valida que la edad sea un número entero
    edad = input("Ingrese la edad (años): ")
    while not edad.isdigit():
        print("La edad debe ser un número entero.")
        edad = input("Ingrese la edad (años): ")

    return nombre, especie, int(edad)


def mostrar_informacion(nombre, especie, edad):
    # Muestra la información registrada de forma organizada
    print("\n------ Información de la mascota ------")
    print("Nombre  :", nombre)
    print("Especie :", especie)
    print("Edad    :", edad, "año(s)")
    print("---------------------------------------\n")


# Punto de entrada: se registra y se muestra la información
nombre, especie, edad = registrar_mascota()
mostrar_informacion(nombre, especie, edad)
