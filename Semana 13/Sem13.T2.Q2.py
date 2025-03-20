def processo(lista):

    ordenada = sorted(lista)
    processada = [
        x * 3 if i % 2 == 0 else x * 5
        for i, x in enumerate(ordenada)
    ]
    return processada


def main():
    lista = []

    print("Digite 100 valores, na qual os impares serem multiplicados por 3 e os pares por 5: ")
    while len(lista) < 100:
        numb = int(input())
        lista.append(numb)

    resultado = processo(lista)

    print(f'A lista ordenada e com os números multiplicados: ')
    print(f'{resultado}')

if __name__ == "__main__":
    main()

