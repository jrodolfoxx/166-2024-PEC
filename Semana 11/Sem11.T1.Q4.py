def inverter(x):
    return int(str(x)[::-1])


def main():
#Entrada
    n = int(input("Digite um número inteiro: "))
#Processo
    resultado = inverter(n)
#Saída
    print(f'O número digitado invertido fica: {resultado}')


if __name__ == '__main__':
    main()