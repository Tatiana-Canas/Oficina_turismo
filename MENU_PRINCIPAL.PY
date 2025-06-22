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
