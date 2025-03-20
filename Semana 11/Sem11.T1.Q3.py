def comaparacao():
    maior = None
    menor = None
    print("Digite uma quantidade indefinida de números inteiros e positivos(0 para encerrar):")
    while True:
#Entrada
        n = int(input())

        if n == 0:
            break

        if maior is None or n > maior:
            maior = n

        if menor is None or n < menor:
            menor = n

    return maior, menor

def main():
#Processo
    maior , menor = comaparacao()
#Saída
    print(f'O maior número é {maior}')
    print(f'E o menor número é {menor}')

if __name__ == '__main__':
    main()
