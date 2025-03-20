def calcular(x):
    if x%2 == 0:
        return (f'Como ele é Par,somarei mais 5, ficará: {x+5}')
    else:
        return (f'Como ele é Impar,somarei mais 8, ficará: {x+8}')

def main():
#Entrada
    n = int(input("Digite um número: "))

#Processo
    resultado = calcular(n)

#Saída
    print(resultado)

if __name__ == '__main__':
    main()
    
