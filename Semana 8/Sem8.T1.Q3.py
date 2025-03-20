def encontrar_maior_menor():
#Entrada
    maior = menor = int(input("Digite o 1* número inteiro: "))
    for i in range(4):
        numero = int(input(f'Digite o {i+2}* número inteiro: '))
        if numero > maior:
            maior = numero 
        if numero < menor:
            menor = numero
    return maior, menor

def main():
#Processo
    maior, menor = encontrar_maior_menor()


#Saída
    print(f'O maior número inteiro é o {maior}')
    print(f'E o menor é o {menor}')

if __name__ == '__main__':
    main()





