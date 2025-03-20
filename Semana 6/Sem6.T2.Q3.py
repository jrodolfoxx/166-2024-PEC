def calcular(x,y):
    total = 3*x+2*y
    return total

def main():
#Entrada
    maca = float(input("Valor da maçã: "))
    banana = float(input("Valor da banana: "))

#Processo
    total = calcular(maca, banana)

#Saída
    print(f'O valor total é R$ {total:.2f}')
   
if __name__ == '__main__':
    main()
