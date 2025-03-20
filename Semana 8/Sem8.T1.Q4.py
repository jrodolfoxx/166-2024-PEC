def calcular(*numeros):
    soma = sum(numeros)
    media = soma/len(numeros)
    return media

    
def main():
#Entrada
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))
    n5 = int(input("Digite o quinto número: "))
    

#Processo
    media = calcular(n1,n2,n3,n4,n5)
#Saída
    print(f'A média desses números é {media:.2f}')
    if n1 > media:
        print(f'{n1:.2f} é maior que a média')
    if n2 > media:
        print(f'{n2:.2f} é maior que a média')
    if n3 > media:
        print(f'{n3:.2f} é maior que a média')
    if n4 > media:
        print(f'{n4:.2f} é maior que a média')
    if n5 > media:
        print(f'{n5:.2f} é maior que a média')
   

if __name__ == '__main__':
    main()
