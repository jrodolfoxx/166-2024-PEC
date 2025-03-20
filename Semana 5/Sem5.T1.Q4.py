def tempo(minutos):
    h = minutos//60
    m = minutos%60
    return h, m

def main():
#Entrada
    t = int(input("Quantidade de minutos: "))

#Processo
    h,m =tempo(t)

#Saída
    print(f'A quantidade de minutos equivale á {h} horas e {m} minutos.')

if __name__ == '__main__':
    main()
