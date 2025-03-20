def ler_lista(tamanho):
    lista = []

    print("Digite 25 números inteiros:")
    for _ in range(tamanho):
        while True:
                numero = int(input())
                lista.append(numero)
                break
    return lista

def intercala_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

def main():
    tamanho_lista = 25

    A = ler_lista(tamanho_lista)

    B = ler_lista(tamanho_lista)

    C = intercala_listas(A, B)

    print(f'Lista A: {A}')
    print(f'Lista B: {B}')
    print(f'Listas intercaladas: {C}')

if __name__ == "__main__":
    main()
