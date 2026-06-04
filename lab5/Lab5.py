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
    
    #parte 3  Haziel
def mostrar_archivo_linea_por_linea():
    print("\n--- CONTENIDO DEL ARCHIVO DE TEXTO ---")

    # Verifica si el archivo existe antes de leerlo
    if not os.path.exists(ARCHIVO_TEXTO):
        print("Todavía no existe el archivo contactos.txt")
        return

    # Abre el archivo en modo lectura
    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        # Muestra cada línea del archivo
        for linea in archivo:
            print(linea.strip())


def mostrar_contactos_ordenados():
    print("\n--- LISTA DE CONTACTOS ---")

    # Carga los contactos desde el archivo de texto
    contactos = cargar_contactos_txt()

    # Si no hay contactos, muestra un mensaje
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    # Ordena los contactos alfabéticamente por nombre
    contactos_ordenados = sorted(contactos, key=lambda c: c["nombre"].lower())

    # Imprime los encabezados de la tabla
    # El formato <5, <25 y <12 ayuda a alinear las columnas
    print(f"{'ID':<5} {'Nombre':<25} {'Teléfono':<12}")
    print("-" * 44)

    # Muestra cada contacto en formato de tabla
    for contacto in contactos_ordenados:
        print(f"{contacto['id']:<5} {contacto['nombre']:<25} {contacto['telefono']:<12}")


