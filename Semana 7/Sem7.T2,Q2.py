def pares(x):
    numero_str = str(x)
    contagem = 0

    for digito in numero_str:
        if int(digito)%2 == 0:
            contagem += 1

    return contagem
   

def main():
#entrada
   numero = int(input("Digite um número entre 100 e 999: "))

#processo
   resultado = pares(numero)

#saída
   print(f'Seu número tem {resultado} dígitos pares.')

if __name__ == '__main__':
    main()
