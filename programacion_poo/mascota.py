# Clase Mascota con sus atributos y métodos

class Mascota:

    def __init__(self, nombre, especie, edad):
        # Atributos de la mascota
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        # Muestra los datos del objeto de forma organizada
        print("\n------ Información de la mascota ------")
        print("Nombre  :", self.nombre)
        print("Especie :", self.especie)
        print("Edad    :", self.edad, "año(s)")
        print("---------------------------------------")

    def hacer_sonido(self):
        # Emite el sonido correspondiente según la especie
        sonidos = {
            "perro": "Guau guau!",
            "gato": "Miau!",
            "pajaro": "Pío pío!",
            "vaca": "Muuu!",
            "pato": "Cuac cuac!",
        }
        sonido = sonidos.get(self.especie.lower(), "...")
        print(f"{self.nombre} dice: {sonido}")
