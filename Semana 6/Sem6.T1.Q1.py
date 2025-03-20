def n_caractere(x):
    q_caractere = len(x)
    return q_caractere

def main():
#Entrada
    nome = input("Digite um nome: ")

#Processo
    q_caractere = n_caractere(nome)

#Saída
    print(f'Esse nome possui {q_caractere} caracteres')

if __name__ == '__main__':
    main()
