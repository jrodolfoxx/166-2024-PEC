def mensagem(x,y,z):
    if x == y and x == z:
        return('Todos os valores são iguais')
    if x != y and x != z and y != z:
        return('Todos os valores são diferentes')
    else: 
        return('Existem dois valores iguais e um diferente')

def main():
#Entrada
    n1 = int(input("Digite o Primeiro número: "))
    n2 = int(input("Digite o Segundo número: "))
    n3 = int(input("Digite o Terceiro número: "))

#Processo
    resultado = mensagem(n1,n2,n3)

#Saída
    print(f'De acordo com os valores, {resultado}.')


if __name__ == '__main__':
    main()