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
