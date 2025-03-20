alfabeto = "abcdefghijklmnopqrstuvxwyz"

#Inserir a letra e a chave para criptografar ou descripografar.
letra = input("Por favor, entre com uma letra para criptografar: ")
chave = int(input("Digite sua chave: "))

posicao = alfabeto.find(letra)

#Use o sinal + para criptografar e - para descriptografar.
nova_posicao = (posicao - chave) % 26

criptografada = alfabeto[nova_posicao]

print("Sua letra criptografada é ", criptografada)