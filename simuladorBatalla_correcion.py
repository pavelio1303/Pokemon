import random 

def fraseAleatoria():
    frases = [
        "¡El ganador de la batalla es increible!",
        "¡La victoria ha sido para el mejor Pokémon!",
        "¡Nuestro ganador ha triunfado en la batalla!",
        "¡Enhorabuena al Pokémon ganador!",
        "¿Quién ganará la próxima vez?"
    ]
    fraseElegida = random.choice(frases)
    return fraseElegida

# Ejercicio 1 prueba Pokemon:

nombrePoke1 = input("Introduce el nombre del pokemon: ")
tipoPoke1 = input("Introduce el tipo del pokemon: ")
nivelpoke1 = int (input("Introduce el nivel del pokemon: "))

if nivelpoke1 < 0:
    nivelpoke1 = 0
if nivelpoke1 > 50:
    nivelpoke1 = 50

print(nombrePoke1 + ", tipo " + tipoPoke1 + ", nivel " + str(nivelpoke1))

nombrePoke2 = input("Introduce el nombre del pokemon: ")
tipoPoke2 = input("Introduce el tipo del pokemon: ")
nivelpoke2 = int (input("Introduce el nivel del pokemon: "))

if nivelpoke2 < 0:
    nivelpoke2 = 0
if nivelpoke2 > 50:
    nivelpoke2 = 50

print(nombrePoke2 + ", tipo " + tipoPoke2 + ", nivel " + str(nivelpoke2))

print(nombrePoke1 + " VS " + nombrePoke2 + " ¡Que comience el combate!")

# Ejercicio 2 prueba Pokemon:

if tipoPoke1 == tipoPoke2 and nivelpoke1 >= nivelpoke2:
    print(f"¡Gana {nombrePoke1}!")
elif tipoPoke1 == tipoPoke2 and nivelpoke1 < nivelpoke2:
    print(f"¡Gana {nombrePoke1}!")
    # A continuación no hace falta comprobar que los tipos sean distintos 
    # ya que, de no serlo, ya se habrían quedado en las líneas anteriores.
elif tipoPoke1 == "Fuego" and nivelpoke2 - nivelpoke1 < 10 :
    print(f"¡Gana {nombrePoke1}!")
elif tipoPoke2 == "Fuego" and nivelpoke1 - nivelpoke2 < 10 :
    print(f"¡Gana {nombrePoke2}!")
# Faltan algunos elif
else:
    print(f"¡Gana {nombrePoke1}!")

##ganador = nombrePoke1

# Ejercicio 3 prueba Pokemon:

##print("Ganador: ¡" + ganador + "!")
print(fraseAleatoria())

# Ejercicio 4 prueba Pokemon:

esJusta = tipoPoke1 == tipoPoke2
if esJusta:
    print("¡Ha sido una batalla justa!")
else:
    print("Vaya abuso... ¡Nada justo!")

