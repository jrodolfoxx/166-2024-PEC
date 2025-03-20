def codigo(x):
    numero = ord(x)
    return numero
def main():
#Entrada
    letra = input("Digite um unico caractere: ")

#Processo
    numero = codigo(letra)

#Saída
    print(f'O código numerico dessa caractere é {numero}')

if __name__ == '__main__':
    main()
