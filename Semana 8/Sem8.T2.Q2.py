def soma(num):
     if 0 < num < 100000:   
         u = num % 10
         num = num // 10 
         d = num % 10
         num = num // 10
         c = num % 10
         num = num // 10
         um = num % 10
         num = num // 10
         dm = num % 10
         num = num // 10
         cm = num % 10
         num = num // 10
         total = u + d + c + um + dm + cm
         return (f'Abaixo de 100000: Então a soma de seus dígitos é {total}')
     else: 
         return (f'Seu número é maior que 100000, então {-1}')


def main():
#Entrada
    num = int(input("Digite um número de sua escolha: "))
    
#Processo
    resultado = soma(num)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()
          
    
