def calcular(numeros):
    soma = sum(numeros)
    media = soma/len(numeros)
    return media
    

def main():
    numeros = []
    for i in range(100):
        numero = int(input())
        numeros.append(numero)

    media = calcular(numeros)

    print(f'{media:.2f}')
    
if __name__ == '__main__':
    main()

