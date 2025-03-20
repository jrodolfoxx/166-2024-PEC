def juros(x, y):
    acumulado = x
    anos = 0
    while acumulado < 2 * x:
        acumulado += acumulado * (y/100)
        anos += 1

    return anos

def main():
#Entrada
    deposito = float(input("Depósito inicial: "))
    taxa = float(input("Taxa de juros ao ano: "))

#Processo
    resultado = juros(deposito, taxa)

#Saída
    print(f'R${deposito} redendo{taxa} ao ano irá dobrar em {resultado} anos')

if __name__ == '__main__':
    main()
