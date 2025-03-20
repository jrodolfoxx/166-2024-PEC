def soma_cumulativa(x):
    acumulativo = []
    soma = 0

    for numero in x:
        soma += numero
        acumulativo.append(soma)
    return acumulativo


def main():
    lista = []

    print("Digite umaa quantidade indeerminada de números reais, use 0 para encerrar:")
    while True:
        numb = int(input())
        if numb == 0:
            break
        lista.append(numb)

    lista_nova = soma_cumulativa(lista)

    print("Nova lista em que cada elemento é a soma dos elementos anteriores:")
    print(lista_nova)

if __name__ == '__main__':
    main()