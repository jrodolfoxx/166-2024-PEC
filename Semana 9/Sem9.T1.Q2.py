def calcular(a,b,c):
    if c == 1:
        return (a+b)
    if c == 2:
        return (a-b)
    if c == 3:
        return (a*b)
    if c == 4:
        return(a/b)

def main():
#Entrada
    n1 = float(input("Primeiro Valor: "))
    n2 = float(input("Segundo Valor: "))
    operacao = int(input("Informe se a operação é Adição(1), Subtração(2), Multiplicaçaõ(3) ou Divisão(4): "))

#Processo
    resultado = calcular(n1,n2,operacao)

#Saída
    print(f'O resultado da operaçaõ é: {resultado}') 

if __name__ == '__main__':
    main()