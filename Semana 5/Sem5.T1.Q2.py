def quadrado(l):
    area = l**2
    perimetro = l*4
    return area, perimetro

def main():
#Entrada
    l = float(input("Digite o valor do lado do quadrado: "))

#Processo
    area, perimetro = quadrado(l)

#Saída
    print(f"A área terá o valor de {area} metros quadrados")
    print(f"E o perimetro o valor de {perimetro} metros")

if __name__ == '__main__':
    main()

    
