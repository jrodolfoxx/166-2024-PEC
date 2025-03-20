def calcular(x,y):
    p1 = 2.50 if x <= 5 else 2.20
    p2 = 1.80 if y <= 5 else 1.50

    total = (x*p1)+(y*p2)

    if x + y > 8 or total > 25.00:
        total *= 0.9

    return total


def main():
#Entrada
    morango = float(input("Qual a quantidade de morangos, em Kg: "))
    maca = float(input("Qual a quantidade de maçãs, em Kg: "))

#Processo
    valor = calcular(morango,maca)

#Saída
    print(f'O preço total a pagar é R$ {valor:.2f}')


if __name__ == '__main__':
    main()