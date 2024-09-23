#Tarea 3 - Nicolas Petit

print("1. M")
print("2. F")
sexo = input("Ingrese el sexo: ")

while sexo != "M" and sexo != "F":
    print("ERROR")
    sexo = input("Vuelva a ingresar el sexo: ")

region = input("Ingrese la region: ")

print("1. Charmander")
print("2. Squirtle")
print("3. Bulbasaur")
pokemon = input("Ingrese su pokemon preferido: ")

while pokemon != "Charmander" and pokemon != "Squirtle" and pokemon != "Bulbasaur":
    print("ERROR")
    pokemon = input("Vuelva a ingresar su pokemon preferido: ")

if sexo == "M":
    print("PERFIL DE ENTRENADOR")
    print("Sexo: Masculino")
    print("Region: ", region)
    print("Pokemon favorito: ", pokemon)
elif sexo == "F": 
    print("PERFIL DE ENTRENADOR")
    print("Sexo: Femenino")
    print("Region: ", region)
    print("Pokemon favorito: ", pokemon)