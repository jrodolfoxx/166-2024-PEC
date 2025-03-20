def genero(nome,sexo):
    if sexo == 1:
        return f'Ilmo Sr. {nome}'
    elif sexo == 2:
        return f'Ilma Sra. {nome}'

def main():
#entrada
    nome = input("Digite seu nome: ")
    sexo = int(input("Se Identifique como masculino(1) ou feminino(2): "))

#processo
    mensagem = genero(nome,sexo)

#saída
    print(f'Olá {mensagem}.')


if __name__ == '__main__':
    main()
