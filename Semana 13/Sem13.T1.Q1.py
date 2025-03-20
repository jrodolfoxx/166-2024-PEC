def ler_numeros():
    numeros = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        while True:
                numero = int(input())
                numeros.append(numero)
                break
    return numeros


def calcular_soma_produto(numeros):
    soma = sum(numeros)
    produto = 1
    for numero in numeros:
        produto *= numero
    return soma, produto


def main():
    numeros = ler_numeros()
    soma, produto = calcular_soma_produto(numeros)

    print(f'Esses foram os números: {numeros}')
    print(f"A soma deles: {soma}")
    print(f"E o produto deles: {produto}")

if __name__ == "__main__":
    main()
