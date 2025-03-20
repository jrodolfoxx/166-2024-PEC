def data(x,y,z,a,b,c):
    if z < c :
        return (f'{a}/{b}/{c}')
    elif c < z:
        return (f'{x}/{y}/{z}')
    elif c == z and y < b:
        return (f'{a}/{b}/{c}')
    elif c == z and b < y:
        return (f'{x}/{y}/{z}')
    elif c == z and b == y and x < a:
        return (f'{a}/{b}/{c}')
    elif c == z and b == y and a < x:
        return (f'{x}/{y}/{z}')
    else:
        return (f'{x}/{y}/{z}')
           
def main():
#Entrada
    print("Primeira data:")
    dia1 = int(input("Dia: "))
    mes1 = int(input("Mês: "))
    ano1 = int(input("Ano: "))
    print("Segunda data: ")
    dia2 = int(input("Dia: "))
    mes2 = int(input("Mês: "))
    ano2 = int(input("Ano: "))

#Processo
    resultado = data(dia1,mes1,ano1,dia2,mes2,ano2)

#Saida
    print(f'Dentre elas, a data mais recente é {resultado}')
   

if __name__ == '__main__':
    main()
