vetorA = list("COMPUTACAO")
vetorB = input("Escreva aqui um texto de 10 letras: ")
for i in range(len(vetorA)):
    if vetorA[i].lower() == vetorB[i].lower():
        print("A letra", vetorB[i], "na posição", i, "é igual à letra de COMPUTACAO.")
