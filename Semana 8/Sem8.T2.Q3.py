def resposta(x):
    if x%3 == 0 and x%5 == 0:
        return 'FIZZBUZZ'
    if x%3 == 0:
        return 'FIZZ'
    if x%5 == 0:
        return 'BUZZ'
    else:
        return (f'O {x} não é divisível por 3 e nem por 5')

def main():
#Entrada
    n = int(input("Digite um número inteiro positivo: "))

#Processo
    resultado = resposta(n)

#Saída
    print(resultado)

if __name__ == '__main__':
    main()
    
