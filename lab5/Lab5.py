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
        
        
        
        
#Victoria:

def buscar_contacto():
    print("\n--- BÚSQUEDA DE CONTACTO ---")

    # Carga los contactos desde el archivo
    contactos = cargar_contactos_txt()

    # Verifica si existen contactos registrados
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    # Solicita el nombre a buscar
    # lower() permite buscar sin importar mayúsculas o minúsculas
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()

    # Valida que el usuario no deje la búsqueda vacía
    if nombre_buscar == "":
        print("Debe ingresar un nombre para buscar.")
        return

    # Variable para saber si se encontró al menos un contacto
    encontrado = False

    # Recorre la lista de contactos
    for contacto in contactos:
        # Busca coincidencias dentro del nombre del contacto
        if nombre_buscar in contacto["nombre"].lower():
            print("\nContacto encontrado:")
            print(f"ID: {contacto['id']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")

            # Cambia a True porque sí encontró un resultado
            encontrado = True

    # Si no encontró nada, muestra un mensaje
    if not encontrado:
        print("No se encontró ningún contacto con ese nombre.")


def contar_contactos():
    # Carga todos los contactos guardados
    contactos = cargar_contactos_txt()

    print("\n--- CONTEO DE CONTACTOS ---")

    # Muestra la cantidad total de contactos registrados
    print(f"Cantidad total de contactos registrados: {len(contactos)}")

    
    
    
    
#Harol: Función de guardar y leer datos binarios además del menú
def guardar_y_leer_binario():
    print("\n--- ARCHIVO BINARIO ---")
    # Si no hay contactos, no se puede generar el archivo binario
    if len(contactos) == 0:
        print("No hay contactos para guardar en archivo binario.")
        return

    try:
        # Abre el archivo binario en modo escritura
        # wb significa write binary
        with open(ARCHIVO_BINARIO, "wb") as archivo:
            # Guarda la lista de contactos en formato binario
            pickle.dump(contactos, archivo)

        print("Contactos guardados en archivo binario correctamente.")

        # Abre el archivo binario en modo lectura
        # rb significa read binary
        with open(ARCHIVO_BINARIO, "rb") as archivo:
            # Recupera los contactos guardados en el archivo binario
            contactos_recuperados = pickle.load(archivo)

        print("\nDatos recuperados desde el archivo binario:")

        # Muestra los contactos recuperados del archivo binario
        for contacto in contactos_recuperados:
            print(f"{contacto['id']} - {contacto['nombre']} - {contacto['telefono']}")

    except (IOError, pickle.PickleError) as e:
        # Captura errores relacionados con archivos o pickle
        print(f"Error al manejar el archivo binario: {e}")


def menu():
    # Bucle principal del sistema
    # Se repite hasta que el usuario elija salir
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE CONTACTOS =====")
        print("1. Registrar contacto")
        print("2. Mostrar archivo de texto línea por línea")
        print("3. Mostrar contactos en tabla")
        print("4. Buscar contacto")
        print("5. Contar contactos")
        print("6. Guardar y leer archivo binario")
        print("7. Salir")

        # Solicita la opción
        opcion = input("Seleccione una opción: ")

        # Ejecuta una función según la opción elegida
        if opcion == "1":
            registrar_contacto()
        elif opcion == "2":
            mostrar_archivo_linea_por_linea()
        elif opcion == "3":
            mostrar_contactos_ordenados()
        elif opcion == "4":
            buscar_contacto()
        elif opcion == "5":
            contar_contactos()
        elif opcion == "6":
            guardar_y_leer_binario()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Inicia el programa llamando al menú principal
menu()

   