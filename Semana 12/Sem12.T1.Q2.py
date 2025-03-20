def compra(x):
    poupoanca = 10000
    renda = 0.007
    taxa = 0.004
    meses =  0

    while poupoanca < x:
        poupoanca += poupoanca * renda
        x += x * taxa
        meses += 1

    return meses


def main():
#Entrada
    carro = float(input("Digite o valor do carro hoje: "))

#Processo
    resultado = compra(carro)

#Saída
    print(f'Em {resultado} meses terá dinheiro suficiente para compra-lo à vista.')


if __name__ == '__main__':
    main()