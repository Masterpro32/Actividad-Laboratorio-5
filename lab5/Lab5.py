#Diego: importación de librerías, definición de archivos y función para cargar contactos

# Importamos os para verificar si existen archivos
import os

# Importamos pickle para guardar y leer datos en archivo binario
import pickle


# Nombre del archivo de texto donde se guardarán los contactos
ARCHIVO_TEXTO = "contactos.txt"

# Nombre del archivo binario donde también se podrán guardar los contactos
ARCHIVO_BINARIO = "contactos.dat"


def cargar_contactos_txt():
    # Lista donde se almacenarán temporalmente los contactos leídos
    contactos = []

    # Verifica si el archivo de texto existe
    # Si no existe, devuelve la lista vacía
    if not os.path.exists(ARCHIVO_TEXTO):
        return contactos

    # Abre el archivo de texto en modo lectura
    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        # Recorre el archivo línea por línea
        for linea in archivo:
            # Elimina espacios o saltos de línea al inicio y final
            linea = linea.strip()

            # Si la línea está vacía, la salta
            if linea == "":
                continue

            # Separa los datos usando la coma como separador
            datos = linea.split(",")

            # Verifica que la línea tenga exactamente 3 datos: id, nombre y teléfono
            if len(datos) == 3:
                # Crea un diccionario con los datos del contacto
                contacto = {
                    "id": datos[0],
                    "nombre": datos[1],
                    "telefono": datos[2]
                }

                # Agrega el contacto a la lista
                contactos.append(contacto)

    # Devuelve la lista de contactos cargados desde el archivo
    return contactos
#Jeanpier: definición de funciones para obtener el siguiente ID y registrar contactos
def obtener_siguiente_id():
    # Carga los contactos existentes
    contactos = cargar_contactos_txt()

    # Si no hay contactos, el primer ID será 1
    if len(contactos) == 0:
        return 1

    try:
        # Toma el ID del último contacto y le suma 1
        ultimo_id = int(contactos[-1]["id"])
        return ultimo_id + 1

    except ValueError:
        # Si ocurre un error al convertir el ID, usa la cantidad de contactos + 1
        return len(contactos) + 1


def registrar_contacto():
    print("\n--- REGISTRO DE CONTACTO ---")

    # Validación del nombre
    while True:
        # Solicita el nombre y elimina espacios innecesarios
        nombre = input("Ingrese el nombre: ").strip()

        # El nombre no puede estar vacío
        if nombre == "":
            print("El nombre no puede estar vacío.")

        # No se permiten comas porque el archivo usa comas para separar datos
        elif "," in nombre:
            print("El nombre no puede contener comas.")

        # Si el nombre es válido, sale del bucle
        else:
            break

    # Validación del teléfono
    while True:
        telefono = input("Ingrese el teléfono: ")

        # Verifica que el teléfono tenga solo números y 9 dígitos
        if telefono.isdigit() and len(telefono) == 9:
            break
        else:
            print("El teléfono debe tener 9 dígitos numéricos.")

    # Genera el ID automáticamente
    nuevo_id = obtener_siguiente_id()

    # Abre el archivo en modo añadir
    # Esto permite agregar contactos sin borrar los anteriores
    with open(ARCHIVO_TEXTO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nuevo_id},{nombre},{telefono}\n")

    print("Contacto guardado correctamente.")
