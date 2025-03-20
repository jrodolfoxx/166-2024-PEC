def operacoes():
    pessoas = 0
    soma = 0 
    menor = None
    maior = None
    print("Digite a idade de cada pessoa(Digite 0 para encerrar).")

    while True:
#Entrada
        idade = int(input())

        if idade == 0:
            break

        pessoas += 1
        soma += idade

        if menor is None or idade < menor:
            menor = idade

        if maior is None or idade > maior:
            maior = idade
#Proceso
    if pessoas > 0:
        media = soma/pessoas
#Saída
        print(f'O total de pessoas é {pessoas}')
        print(f'A média das idades: {media:.2f}')
        print(f'A menor idade é {menor}')
        print(f'E a maior idade é {maior}')

def main():
    operacoes()


if __name__ == '__main__':
    main()