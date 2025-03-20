def calcular(x):
    numeros = str(x)
    soma = 0

    for digito in numeros:
        soma += int(digito)

    return soma

def main():
#Entrada
    data = int(input("Digite sua data de nascimento na forma 00000000: "))

#Processo
    resultado = calcular(data)

#Saaída
    print(f'O seu número da sorte é: {resultado}')

if __name__ == '__main__':
    main()