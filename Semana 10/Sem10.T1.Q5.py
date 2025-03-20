def conjunto(x):
    maior = 0
    for i in range(x):
        nota = int(input())
        if nota > maior:
            maior = nota
    return maior


def main():
    melhor = conjunto(100)

    print(melhor)

if __name__ == '__main__':
    main()