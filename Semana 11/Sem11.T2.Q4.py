def exibir():
    print('CÓDIGO  PRODUTO         PREÇO (R$)')
    print('H       Hamburger       5,50')
    print('C       Cheeseburger    6,80')
    print('M       Misto Quente    4,50')
    print('A       Americano       7,00')
    print('Q       Queijo Prato    4,00')
    print('X       PARA TOTAL DA CONTA')



def calcular():
    menu = {
        'H': 5.50,
        'C': 6.80,
        'M': 4.50,
        'A': 7.00,
        'Q': 4.00
    }

    total = 0
    print("Faça seu pedido(Digite X para encerrar).")
    while True:
        exibir()
#Entrada
        codigo = input().upper()[0]

        if codigo == "X":
            break

        elif codigo in menu:
            total += menu[codigo]
        else:
            print("Opção inválida.") 
    return total



def main():
#Processp
    resultado = calcular()
#Saída
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
