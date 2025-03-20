def ordem(x):
    digito1 = x//10
    digito2 = x%10
    contador = 0
    if digito1%2 != 0:
        contador += 1
    if digito2%2 != 0:
        contador += 1
        
    if contador == 0:
        return 'Nenhum dígito é ímpar.'
    elif contador == 1:
        return 'Apenas um dígito é ímpar.'
    else:
        return 'Os dois dígitos são ímpares.'
        
   
def main():
#Entrada
    numero = int(input("Digite um número: "))

#Processo
    resultado = ordem(numero)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()
