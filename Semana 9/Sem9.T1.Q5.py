def determinar(x):
    r = x%5
    if r == 0:
        return (f'{(9*x)+7}')
    if r == 1:
        if x%2 == 0:
            return('par')
        else:
            return('ímpar')
    if r == 2:
        cal =  5*(x**2) - (3*x) + 42
        return (cal)
    if r == 3:
        return (f'{x//10}')
    if r == 4:
        return(f'{x**2}')


def main():
#Entrada
    n1 = int(input("Digite um número que irá ser dividido por 5: "))

#Processo
    resultado = determinar(n1)

#Saída
    print(f'De acordo com o resto da divisão o resultado é : {resultado}.')


if __name__ == '__main__':
    main()