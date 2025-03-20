def calcular(x,y,z,a,b,c):
    idade = z - c
    if y < b:
        idade -= 1
    elif y == b and x < a:
        idade -= 1
    return idade
    


def main():
#Entrada
    dia_a = int(input("Dia atual: "))
    mes_a = int(input("Mês atual: "))
    ano_a = int(input("Ano atual: "))
    dia_n = int(input("Dia de nascimento: "))
    mes_n = int(input("Mês de nascimento: "))
    ano_n = int(input("Ano de nascimento: "))

#Processo
    resultado = calcular(dia_a,mes_a,ano_a,dia_n,mes_n,ano_n)

#Saída
    print(f'A idade dessa pessoa é {resultado} anos')

if __name__ == '__main__':
    main()

    
