def calcular(a,b,c):
    return 2*a+5*b-c

def main():
#Entrada
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    z = int(input("Digite o terceiro número: "))

#Processo
    r =calcular(x,y,z)

#Saída
    print(f'O resultado na função é {r}')

if __name__ == '__main__':
    main()
