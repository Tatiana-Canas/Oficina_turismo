#turistas_por_mes()

def turistas_por_mes():
    mes_buscado = input("Ingrese el número del mes a buscar (01 a 12): ").strip().zfill(2)
    encontrados = False
    print(f"\nTuristas que visitaron en el mes {mes_buscado}:")
    for id_turista, datos in turistas.items():
        nombre, pais, fecha = datos
        partes_fecha = fecha.split("-")  # ['8', '03', '2024'] o ['12', '01', '2024']
        mes = partes_fecha[1]  # El segundo elemento siempre es el mes
        if mes == mes_buscado:
            print(f"ID: {id_turista} | Nombre: {nombre} | País: {pais} | Fecha: {fecha}")
    if not encontrados:
        print("No hay turistas registrados para ese mes.")
