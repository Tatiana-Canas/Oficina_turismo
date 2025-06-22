#CREACION DICCIONARIO TURISTAS CON LISTA DE 3 ITEMS:NOMBRE,PAIS,FECHA INGRESO. KEY :"001"
turistas={"001": ["John Doe", "Estados Unidos", "12-01-2024"],
          "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
          "012": ["Julian Martinez", "Argentina", "19-09-2023"],
          "014": ["Agustin Morales", "Argentina", "8-03-2024"],
          "005": ["Garcia", "Mexico", "10-05-2024"],
          "006": ["Maria Lopez", "Mexico", "08-12-2023"],
          "007": ["Joao Silva", "Brasil", "20-06-2024"],
	      "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	      "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
          "008": ["Ana Santos", "Brasil", "03-10-2023"],
          "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
          "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
          }






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