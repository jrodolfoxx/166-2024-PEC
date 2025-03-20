def somatorio():
    soma = 0
    print("Digite números inteiros(Digite 0 para encerrar).")

    while True:
#Entrada
        n = int(input())

        if n == 0:
            break

        soma += n

    return soma

def main():
#Processo
    resultado = somatorio()
#Saída
    print(f'A soma desses números resultará em {resultado}')

if __name__ == '__main__':
    main()