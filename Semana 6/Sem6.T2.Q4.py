def espaciais(x):
    idade_e = x//2
    return idade_e

def main():
#Entrada
    idade_t = int(input("Idade em anos terrestre: "))

#Processo
    idade_e = espaciais(idade_t)

#Saída
    print(f'Essa idade em anos espaciais equivale a {idade_e} anos')
   
if __name__ == '__main__':
    main()
