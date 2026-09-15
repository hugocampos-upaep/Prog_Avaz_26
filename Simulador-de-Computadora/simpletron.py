# Simpletron - Primera versión

memory = [0] * 100

# Registros
accumulator = 0
instructionCounter = 0
instructionRegister = 0
operationCode = 0
operand = 0

print("*** ¡Bienvenido a Simpletron! ***")
print("*** Introduzca su programa una instrucción a la vez ***")
print("*** Teclee 9999 para terminar la carga ***")
print()

posicion = 0

# Carga del programa
while posicion < 100:

    valor = int(input(f"{posicion:02d} ? "))

    if valor == 9999:
        break

    if valor < -9999 or valor > 9998:
        print("Valor fuera de rango.")
        continue

    memory[posicion] = valor
    posicion += 1

print()
print("*** Se terminó de cargar el programa ***")
print("*** Comienza la ejecución del programa ***")
print()

for i in range(posicion):
    print(f"{i:02d}: {memory[i]:+05d}")
