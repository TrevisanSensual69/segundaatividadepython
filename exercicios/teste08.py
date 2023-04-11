nome = input("Digite o nome completo: ")
genero = input("Digite o sexo (M/F/Traveco): ")
idade = int(input("Digite a idade: "))
if genero.upper() == "F" and idade < 25:
    print(nome, "ACEITA")
else:
    print("NÃO ACEITA (pq vc é homem ou traveco, apesar que traveco é homem só que usa roupa de mulher)")
