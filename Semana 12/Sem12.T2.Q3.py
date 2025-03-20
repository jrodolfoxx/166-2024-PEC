def calcular(x):
    h = 0
    for i in range(1, x + 1):
        h += 1 / i
    return h

def main():
#Entrada
    n = int(input("Digite um número para o valor de N: "))

#Processo 
    valor = calcular(n)

#Saída
    print(f'O valor de H é igual à: {valor:.4f}')

if __name__ == '__main__':
    main()