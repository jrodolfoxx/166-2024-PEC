def fabrica(x):
    minutos = x//60
    segundos = x%60
    hora = minutos//60
    restante = minutos%60
    return f'{hora:02}:{restante:02}:{segundos:02}'



def main():
#Entrada
    tempo = int(input())

#Processamento
    resultado = fabrica(tempo)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()