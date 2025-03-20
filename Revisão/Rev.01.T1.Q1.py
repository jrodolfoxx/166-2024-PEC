def compra(x, y):
    if x < y :
        troco = y-x
        return (f'{troco:.2f}')
    if x == y:
        troco = y-x
        return(f'{troco:.2f}')
    else:
        return (f'Pagamento Insuficiente')


def main():
#Entrada
    valor = float(input())
    pago = float(input())

#Processamento
    resultado = compra(valor, pago)

#Saida
    print(resultado)



if __name__ == '__main__':
    main()