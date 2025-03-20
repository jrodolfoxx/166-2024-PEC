def armazenar():
    numeros = []
    impar = []
    par = []

    print("Digite 20 números inteiro: ")
    for _ in range(20):
        n = int(input())
        numeros.append(n)
        if n %2 == 0:
            par.append(n)
        else:
            impar.append(n)

    return numeros, impar, par

def main():
    numeros, impar, par = armazenar()

    print(f'Todos os números: {numeros}')
    print(f'Os números pares: {par}')
    print(f'Os números impares: {impar}')

if __name__ == '__main__':
    main()