def evento(x):
    h = x//3600
    r = x%3600
    m = r//60
    s = r%60
    return h,m,s

def main():
#Entrada
    segundos = int(input("Digite o tempo em segundos na fábrica: "))

#Processo
    h,m,s = evento(segundos)

#Saída
    print(f'É equivalente a {h} horas,{m} minutos e {s} segundos')

if __name__ =='__main__':
    main()
