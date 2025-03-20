def numero(x):
    resultado = x % 2
    if resultado == 0:
        return False
    elif resultado == 1:
        return True

def main():
#entrada
   valor = int(input("Digite um número: "))
   
#processo
   booleano = numero(valor)

#saída
   print(f'Seu valor é {booleano}')


if __name__ == '__main__':
    main()
