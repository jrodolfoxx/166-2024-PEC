def comprar(x,y):
     pago = x*y
     return pago


def main():
#Entrada
     valor = float(input())
     consumido = float(input())

#Processamento
     resultado = comprar(valor, consumido)

#Saida
     print(f'{resultado:.2f}')


if __name__ == '__main__':
    main()