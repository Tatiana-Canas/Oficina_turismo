#CREACION DICCIONARIO TURISTAS CON LISTA DE 3 ITEMS:NOMBRE,PAIS,FECHA INGRESO. KEY :"001"
turistas={"001": ["John Doe", "Estados Unidos", "12-01-2024"],
          "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
          "012": ["Julian Martinez", "Argentina", "19-09-2023"],
          "014": ["Agustin Morales", "Argentina", "08-03-2024"],
          "005": ["Garcia", "Mexico", "10-05-2024"],
          "006": ["Maria Lopez", "Mexico", "08-12-2023"],
          "007": ["Joao Silva", "Brasil", "20-06-2024"],
	      "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	      "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
          "008": ["Ana Santos", "Brasil", "03-10-2023"],
          "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
          "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
          }

#FUNCION TURISTAS POR PAIS
def turistas_por_pais():
    pais_buscado = input("Ingrese el país a buscar en Turistas: ").strip().lower()
    encontrados = False
    print(f"\nTuristas provenientes de {pais_buscado.title()}:")
    for id_turista, datos in turistas.items():
        nombre, pais, fecha = datos
        if pais.lower() == pais_buscado:
            print(f"ID: {id_turista} | Nombre: {nombre} | País: {pais} | Fecha: {fecha}")
            encontrados = True
    if not encontrados:
        print("No hay turistas registrados de ese país.")

#turistas_por_mes()
def turistas_por_mes():
    mes_buscado = input("Ingrese el número del mes a buscar (1 a 12): ").strip()

    # Validar que sea un número válido del 1 al 12
    if not mes_buscado.isdigit() or not (1 <= int(mes_buscado) <= 12):
        print("❌ Mes inválido. Ingrese un número del 1 al 12.")
        return
    
    mes_buscado = mes_buscado.zfill(2)  # Convertimos '2' → '02' para comparar con fechas
    encontrados = []

    for id_turista, datos in turistas.items():
        nombre, pais, fecha = datos
        partes_fecha = fecha.strip().split("-")

        if len(partes_fecha) == 3:
            _, mes, _ = partes_fecha
            mes = mes.zfill(2)  # Asegura comparación correcta
            if mes == mes_buscado:
                encontrados.append(f"ID: {id_turista} | Nombre: {nombre} | País: {pais} | Fecha: {fecha}")
        else:
            print(f"⚠️ Fecha mal formateada para turista ID {id_turista}: {fecha}")

    if encontrados:
        print(f"\nTuristas que visitaron en el mes {int(mes_buscado)}:")
        for turista in encontrados:
            print(turista)
    else:
        print("No hay turistas registrados para ese mes.")  


# Funcion Eliminar Turista
def eliminar_turista():
    nombre_buscado = input("Ingrese el nombre del turista a eliminar: ").strip().lower()
    encontrado = False

    # Recorremos el diccionario para encontrar el nombre
    for id_turista in list(turistas.keys()):  # Usamos list() para evitar errores al modificar el diccionario durante el recorrido
        nombre = turistas[id_turista][0]
        if nombre.lower() == nombre_buscado:
            del turistas[id_turista]
            print("Turista eliminado con éxito.")
            encontrado = True
            break #(Se elimina el primer turista que coincide  el nombre)
    if not encontrado :
        print("Turista no encontrado. No se pudo eliminar.") 


# Menu_principal(Main)
while True:
    print("***MENU PRINCIPAL TURISTAS***")
    print("1.- Turistas por pais.")
    print("2.- Turistas por mes.")
    print("3.- Eliminar turistas.")
    print("4.- Salir.")

    opcion=input(" Ingrese su opción entre 1 y 4:  ")
    if opcion=="1" :
        turistas_por_pais()
    elif opcion=="2" :
        turistas_por_mes()
    elif opcion=="3":
        eliminar_turista()
    elif opcion=="4" :
        print(" Programa terminado... ")
        break
    else:
        print(" Ingrese sólo valores dentro del rango 1 a 4")



