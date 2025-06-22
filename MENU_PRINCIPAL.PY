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