def zero(x):
    lista = [0] * x
    print(f'Lista com {x} zeros: {lista}')
    return lista


def sequencia(x):
    lista = list(range(1, x+1))
    print(f'Lista com sequência de 1 a {x}: {lista}')
    return lista


def teclado(x):
    lista = []
    print(f'Por favor, insira {x} valores:')
    for i in range(x):
        valor = int(input(f"valor do {i+1}:"))
        lista.append(valor)
    print(f'Lista com os valores inseridos: {lista}')
    return lista


def invertido(x):
    lista = []
    print(f"Digite {x} valores para serem invertidos:")
    for i in range(x):
        valor = int(input(f'Valor {i+1}: '))
        lista.insert(0, valor)
    print(f'Lista com o valores na ordem inversa: {lista}')
    return lista


def main():
    n = int(input("Digite quantos valores devem ser processados: "))

    zero(n)

    sequencia(n)

    teclado(n)

    invertido(n)

if __name__ == '__main__':
    main()
