print("¡Vamos a simular un combate!")
nombrePoke1 = input("Introduce el nombre del primer pokemon: ")
tipoPoke1 = input("Introduce su tipo [solo entre 'Agua', 'Fuego' y 'Planta']: ")
# CELIA: Tenías que pasarlo a entero, ya es str.
nivelPoke1 = str(input("Introduce su nivel [Entre 0 y 50]: "))
print("¡Ahora vamos con el segundo!")
nombrePoke2 = input("Introduce el nombre del segundo pokemon: ")
tipoPoke2 = input("Introduce su tipo [solo entre 'Agua', 'Fuego' y 'Planta']: ")
nivelPoke2 = str(input("Introduce su nivel [Entre 0 y 50]: "))

# CELIA: Podías haberle llamado directamente así al solicitarlas por pantalla.
tipo1 = tipoPoke1
tipo2 = tipoPoke2
ganador = nombrePoke1
nivel1 = nivelPoke1

# CELIA: Para hacer las operaciones lógicas necesitas números, no str.
if nivelPoke1 > str(50):
    nivel1 = 50
elif nivelPoke1 < str(0):
    nivel1 = 0

if tipo1 == tipo2 and nivelPoke1 < nivelPoke2:
    ganador = nombrePoke2
elif tipo1 != tipo2 and nivelPoke1 == nivelPoke2:
    if tipo1 == "Fuego" and tipo2 != "Fuego":
        print("Ganador " + str(nombrePoke1))
    elif tipo2 == "Fuego" and tipo1 != "Fuego":
        print("Ganador " + str(nombrePoke2))
    else:
        print(Empate)
elif tipo1 != tipo2 and nivelPoke1 != nivelPoke2:
    if tipo1 == "Fuego" and tipo2 != "Fuego" and (nivelPoke2 > (nivelPoke1 + 10)):
        print("Ganador " + str(nombrePoke2))
    elif tipo1 != "Fuego" and tipo2 == "Fuego" and (nivelPoke1 > (nivelPoke2 + 10)):
        print("Ganador " + str(nombrePoke1))
    elif tipo1 != "Fuego" and tipo2 != "Fuego" and (nivelPoke1 > nivelPoke2):
        print("Ganador " + str(nombrePoke1))
    elif tipo1 != "Fuego" and tipo2 != "Fuego" and (nivelPoke2 > nivelPoke1):
        print("Ganador " + str(nombrePoke2))








