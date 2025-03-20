def valor(x):
    aproximar = round(x)
    return aproximar

def main():
   dinheiro = float(input("Digite sua quantidade de dinheiro: "))

   aproximar = valor(dinheiro)

   print(f'Esse valor arredondado é igual a R$ {aproximar}')

if __name__ == '__main__':
    main()
