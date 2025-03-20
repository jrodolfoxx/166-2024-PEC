def numeros(x,y,z):
    n1 = max(x,y,z)
    n2 = min(x,y,z)
    n3 = (x+y+z)-(n1+n2)
    return (f'{n2},{n3},{n1}')
   
    return 


def main():
#Entrada
    a = int(input("Escolha seu primeiro número: "))
    b = int(input("Escolha seu segundo número: "))
    c = int(input("Escolha seu terceiro número: "))

#Processo
    resultado = numeros(a,b,c)

#Saída
    print(f'A ordem crescente desses números é {resultado}.')


if __name__ == '__main__':
    main()
