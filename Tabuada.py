tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

tabuadas = int(input("Digite um número para a tabuada: "))
print("Tabuada do número: ", tabuadas)
for valors in range(1,11,1):
    print(tabuadas, " X ", valors, " = ", tabuadas * valors)