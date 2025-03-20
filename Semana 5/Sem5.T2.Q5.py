def v_letra(caractere):
#Processo
    if caractere.lower()in 'abcdefghijklmnopqrstuvwxyz0123456789':
        return False
    else:
        return True

def main():
#Entrada
    caractere = input("Digite uma caractere: ")
#Saída
    print(f'Ela é {v_letra(caractere)} para esse código')


if __name__ == '__main__':
    main()
