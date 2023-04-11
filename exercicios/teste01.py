palavra = input("Digite um texto com no máximo 10 letras: ")
vogais = "aeiou"
cont = 0
for letra in palavra:
    if letra in vogais:
        cont += 1
print("O texto", palavra, "possui", cont, "vogais.")
