# Sistema de Gestión de Mascotas

**Nombre del estudiante:** José Alberto Tarco Tipán

## Descripción

Este proyecto contiene dos soluciones desarrolladas en Python para gestionar
la información básica de una mascota: **nombre**, **especie** y **edad**.
Cada solución aborda el problema desde un enfoque de programación distinto.

### Programa 1: Programación Tradicional
Carpeta `programacion_tradicional/`, archivo `tradicional.py`.

Resuelve el problema utilizando únicamente **funciones y variables**, sin clases
ni objetos. La función `registrar_mascota()` solicita los datos al usuario por
teclado e incluye una validación para la edad. La función `mostrar_informacion()`
presenta los datos de forma ordenada en pantalla.

### Programa 2: Programación Orientada a Objetos
Carpeta `programacion_poo/`, archivos `mascota.py` y `main.py`.

Define la clase **`Mascota`** con los atributos `nombre`, `especie` y `edad`,
y los métodos `mostrar_informacion()` y `hacer_sonido()`. En `main.py` se
instancian dos objetos de la clase y se ejecutan sus métodos, evidenciando el
uso de clase, objeto, atributos, métodos y abstracción.

## Estructura del repositorio

```
├── programacion_tradicional/
│   └── tradicional.py
├── programacion_poo/
│   ├── main.py
│   └── mascota.py
└── README.md
```

## Ejecución

Requiere **Python 3**.

```bash
# Programa tradicional
cd programacion_tradicional
python tradicional.py

# Programa orientado a objetos
cd programacion_poo
python main.py
```

## Reflexión

Desarrollar el mismo problema con ambos enfoques permite identificar diferencias
importantes entre los dos estilos de programación.

En la programación tradicional, los datos y las acciones están separados: las
variables viajan como parámetros entre funciones. Es un enfoque directo y
sencillo, adecuado para problemas pequeños.

En la programación orientada a objetos, los datos y los comportamientos se
agrupan dentro de la clase `Mascota`, formando una unidad completa. Esto
facilita la organización del código y su crecimiento futuro: si se necesita
agregar un nuevo atributo o método, basta con modificar la clase.

En conclusión, la programación tradicional resulta más simple para problemas
puntuales, mientras que la programación orientada a objetos ofrece mayor orden,
reutilización y facilidad de mantenimiento a medida que el proyecto crece.
