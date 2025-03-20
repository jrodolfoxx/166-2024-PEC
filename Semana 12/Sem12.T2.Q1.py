def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)
    
def main():
#Entrada
     numero = int(input("Digite um número: "))

#Processo
     resultado = fatorial(numero)

#Saída
     print(f'O Fatorial desse número é: {resultado}')

if __name__ == '__main__':
    main()