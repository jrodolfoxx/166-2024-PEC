def n_caractere(x):
    s_espaco = x.strip()
    q_caractere = len(s_espaco)
    return q_caractere

def main():
#Entrada
    frase = input("Digite uma frase :")

#Processo
    q_caractere = n_caractere(frase)

#Saída
    print(f'Essa frase contém {q_caractere} caracteres')

if __name__ == '__main__':
    main()
