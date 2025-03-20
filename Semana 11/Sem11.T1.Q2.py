def aritmetica():
    soma = 0
    contagem = 0
    print("Digite números inteiros positivos(Digite 0 para encerrar).")
    while True:
#Entrada
        n = int(input())

        if n == 0:
            break

        if n > 0:
            soma += n 
            contagem += 1

    if contagem > 0:
        media = soma/contagem
        return media
    else:
        return None
    
def main():
#Processo
    media = aritmetica()
#Saída
    if media is not None:
        print(f'A média aritmética desses números é: {media:.2f}')

if __name__ == '__main__':
    main()

