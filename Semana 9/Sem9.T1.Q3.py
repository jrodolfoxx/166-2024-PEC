def verificar(x,y):
    if x == y:
        return ('QUADRADO')
    else:
        p = (x*2)+(y*2)
        a = x*y
        return(f'{p:.0f} o perimetro - {a:.0f} a área')


def main():
#Entrada
    base = float(input("Valor da Base: "))
    altura = float(input("E o Valor da Altura: "))

#Processo
    resultado = verificar(base,altura)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()