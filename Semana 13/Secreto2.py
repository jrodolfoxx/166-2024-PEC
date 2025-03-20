alfabeto = "abcdefghijklmnopqrstuvxwyz"

mensagem = input("Por favor, insira a mensagem para ser criptografada: ").lower()
criptografada =""
chave = int(input("Digite a chave: "))

for char in mensagem:
    if char in alfabeto:
        posica = alfabeto.find(char)
        nova = (posica + chave) % 26

        criptografada = criptografada + alfabeto[nova]

    else:
        criptografada = criptografada + char

    print("Sua mensagem criptografada é ", criptografada)