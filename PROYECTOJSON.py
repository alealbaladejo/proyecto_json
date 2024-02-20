import json 
with open ("EQUIPOS.json", "r") as archivo:
    datos = json.load(archivo)
def menu(datos_partido):
    print(''' -------MENU-------
    OPCiON 1 -- Lista de equipos.
    OPCiON 2 -- Mostrar el total de goles marcados en todos los partidos
    OPCiON 3 -- Solicitar un equipo y mostrar todos los partidos en los que ese equipo ha participado
    OPCiON 4 -- Pedir un comentario y mostrar el partido asociado, incluyendo detalles sobre los equipos que jugaron.
    OPCiON 5 -- ingresar un equipo y devolver la cantidad de veces que ha jugado como local y como visitante en todos los partidos.''')

    return

def listar_equipos(datos_partidos):
    equipos = set()
    for partido in datos_partidos:
        a = partido["teams"]
        for equipo in a:
            equipos.add(equipo)   
    
    print("________________\nLiSTA DE EQUIPOS\n________________\n")
    print(len(equipos))
    
    for nombre in equipos:
        print(nombre)

def contar_goles (datos_partidos):
    totalgoles = 0
    goleslocal=0
    golesvisit=0
    for partido in datos_partidos:
        for  equipo, gol in partido['goals'].items():
            totalgoles += gol
        goleslocal += partido['goals'][partido['teams'][0]]
        golesvisit += partido['goals'][partido['teams'][1]]
            #print (f"Equipo : {equipo}\n GOLES MARCADOS: {gol}\n GOLES TOTALES: {totalgoles}")
    print (f"\n\nEl total de goles marcados de todos los equipo es de {totalgoles}")
    print (f"Como local se han marcado {goleslocal}")
    print (f"Como visitante se han marcado {golesvisit}")
    return totalgoles

def buscar_partidos(datos_partidos):
    equipo = input("Ingresa el nombre de un equipo: ")
    lista_partidos = []

    for datos in datos_partidos:
        if equipo in datos["teams"]:
            lista_partidos.append(datos["teams"])

    if len(lista_partidos) == 0:
        print(f"El equipo {equipo} no ha participado en ningún partido.")
    else:
        print(f"Partidos de {equipo}:")
        for i, partido in enumerate(lista_partidos, start=1):
            print(f"Partido {i}: {partido[0]} - {partido[1]}\n")
        return lista_partidos

def comentario(datos_partidos):
    comentario_buscar = input("Ingresa un comentario: ")

    for partido in datos_partidos:
        comentarios_partido = partido.get("comments", [])
        for comentario in comentarios_partido:
            #print (comentario)
            if comentario["comment_text"] == comentario_buscar:
                print("Detalles del partido:")
                print(f"ID del partido: {partido['match_id']}")
                print(f"Equipos: {', '.join(partido['teams'])}")
                print(f"Hora de inicio: {partido['kickoff_time']}")
                print(f"Descripción: {partido['match_description']}")
                print(f"Goles: ")
                for equipo, goles in partido['goals'].items():
                    print(f"{equipo} : {goles} goles")
                print(f"Comentarios:")
                
                for comentario in partido['comments']:
                    print(f"  - {comentario['commentator']}: {comentario['comment_text']}")
                
                print(f"Compartidos: {partido['shares']}")
                print(f"Ubicación: {partido['location']}")
                return comentario["comment_text"]

    print("No se encontró ningún partido asociado al comentario.")

def local_visitante(datos_partidos):
    equipoABuscar=input("Ingresa el nombre de un equipo: ")
    contlocal = 0
    contvisit = 0
    for datos in datos_partidos:
        if equipoABuscar in datos["teams"]:
            print ("Local: ",datos['teams'][0],"\nVisitante: ",datos['teams'][1])
            if equipoABuscar == datos["teams"][1]:

                #print (f"{equipoABuscar} este partido juega como visitante.")
                contvisit+=1
            if equipoABuscar == datos["teams"][0]:

                #print (f"{equipoABuscar} este partido juega como local.")
                contlocal+=1
    print (f"{equipoABuscar} ha jugado como local un total de {contlocal} veces.")
    print (f"{equipoABuscar} ha jugado como visitante un total de {contvisit} veces.")





num=0
while num != 6:
    dato = menu(datos)
    num = int(input ("ingresa una opción: "))
    
    if num == 1:
        dato = listar_equipos(datos)

    elif num == 2:
        dato = contar_goles(datos)
        
    elif num == 3:
        dato = buscar_partidos(datos)

    elif num == 4:
        dato = comentario(datos)

    elif num == 5:
        dato = local_visitante(datos)
    else:
        print ("El número introducido no es una opción.")