def temperatura(x):
    fah = (x*(9/5))+32
    return fah

def main():
#Entrada
    celsius = float(input("Temperatura em Celsius: "))

#Processo
    fah = temperatura(celsius)

#Saída
    print(f'É equivalente a {fah:.2f} graus Fahrenheit')
   
if __name__ == '__main__':
    main()
