def determinar(x,y,z):
    seg = abs(x - y)
    ter = abs(x - z)
    if seg < ter:
        return seg
    else:
        return ter


def main():
#Entrada
    n1 = int(input("Digite o Primeiro valor: "))
    n2 = int(input("Digite o Segundo valor: "))
    n3 = int(input("Digite o Terceiro valor: "))

#Processo
    resultado = determinar(n1,n2,n3)

#Saída
    print(f'A menor diferença é {resultado}.')


if __name__ == '__main__':
    main()