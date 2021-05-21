# o una función recursiva debe calcular
# cuantas letras tiene el nombre y el apellido de cada empleado, ejemplo:
# Nombre: PEDRO Apellido: PINEDA
# P:2
# E:2
# D:2
# R:1
# O:1
# I:1
# N:1
# A:1

# def addValue(a, v):
#     a.append(v)
#     return a 


def counterLetters(full, letterCounter, counter): 

    if counter == len(full) : 
        return letterCounter
    else :
        if full[counter] in letterCounter :
            letterCounter[full[counter]] += 1 
        else : 
            letterCounter[full[counter]] = 1 
        counter += 1 
        return counterLetters(full, letterCounter, counter)
    

if __name__ == "__main__": 
    name = input('Nombre : ')
    surname = input('Apellido : ')

    full = name + surname
    full = full.upper()
    counter = 0 
    letterCounter = {}

    print(counterLetters(full, letterCounter, counter))

    # Sanchez

