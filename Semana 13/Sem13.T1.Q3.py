def reais(x):
    lista = []
    if x == 0:
        print("[]")
    else:
        print(f"Digite {x} valores reais:")
        for i in range(x):
            valor = float(input())
            lista.append(valor)

        inversos = [f'{valor}' for valor in reversed(lista)]
        print(f"Os valores lidos na ordem inversa: [{', '.join(inversos)}]")


def escola(x):
    if x == 0:
        print("[]")
        print("SEM NOTAS")
        return
    else:
        print(f"Digite {x} notas:")
        notas = []
        for i in range(x):
            nota = float(input())
            notas.append(nota)

    media = sum(notas)/x
    formatada = [f'{nota:.1f}' for nota in notas]
    print(f"As notas: [{', '.join(formatada)}]")
    print(f'A média entre elas: {media:.1f}')
   

def letras(x):
    vogais = 'aeiouAEIOU'
    consoantes = []
    total = 0

    print(f"Digite {x} letras: ")
    for i in range(x):
        letra = input()[0]
        if letra in vogais:
            total += 1
        elif letra.isalpha():
            consoantes.append(letra)

    print(f'Total de vogais: {total}')
    formatadas = ', '.join([f"'{consoante}'" for consoante in consoantes])
    print(f"As consoantes: [{formatadas}]")


def main():
    n = int(input("Digite quantos valores vc quer adicionar: "))

    reais(n)

    escola(n)

    letras(n)


if __name__ == '__main__':
    main()