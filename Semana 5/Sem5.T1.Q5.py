def numero_inverso():
#Entrada
    numero = int(input("Digite o número deseado: "))
#Proceso
    if 1000<=numero<=9999:
        numero_inverso = int(str(numero)[::-1])
        return numero_inverso

def main():
    resultado=numero_inverso()
#Saída
    print(f'Seu número invertido será {resultado}')

if __name__ == '__main__':
    main()
