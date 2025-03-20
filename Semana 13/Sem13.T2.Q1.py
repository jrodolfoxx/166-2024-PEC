def multiplica_constante(lista, constante):
    nova = [x * constante for x in lista]
    return nova
 

def main():
    lista = []

    print("Digite valores a desejar, digite 0 para encerrar:")
    while True:
        numb = int(input())
        if numb == 0:
            break
        lista.append(numb)

    constante = int(input("Digite o valor da constante: "))

    nova_lista = multiplica_constante(lista, constante)

    print(f'A nova lista: {nova_lista}')

if __name__ == "__main__":
    main()

 

 