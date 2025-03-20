def conta(x, y):
    mes = 10
    ano = 2016

    while y <= x:
        mes += 1

        if mes > 12:
            mes = 1
            ano +=1
        
        if mes == 3:
            x *= 1.05

        y *= 1.15

    return mes, ano
def main():
#Entrada
    salario = float(input("Valor do salário: "))
    divida = float(input("Valor da dívida: "))
#Processo
    mes, ano = conta(salario, divida)
#Saída
    print(f'"A dívida será superior ao salário em {mes}/{ano}')

if __name__ == '__main__':
    main()