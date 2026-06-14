# Archivo principal: crea objetos de la clase Mascota y ejecuta sus métodos
from mascota import Mascota

print("====== Sistema de gestión de mascotas ======")

# Se crean dos objetos de la clase Mascota
mascota1 = Mascota("Toby", "Perro", 5)
mascota2 = Mascota("Nala", "Gato", 2)

# Se ejecutan los métodos de cada objeto
for mascota in [mascota1, mascota2]:
    mascota.mostrar_informacion()
    mascota.hacer_sonido()
