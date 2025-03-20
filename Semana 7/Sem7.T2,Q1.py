def caractere(n1, n2= None):
    if n2:
        return len(n1) + len(n2)
    else:
        return len(n1)

def main():
#entrada
    nome = input("Digite o seu nome: ").strip()
    civil = int(input("Digite seu estado civil como 1(casado) e 2 (solteiro): "))
#processo
    if civil == 1 :
        conjugue = input("Qual seu nome de conjugue: ").strip()
        total = caractere(nome,conjugue)
    else:
        total = caractere(nome)

#saída
    print(f'Existem {total} caractere no(s) nome(s).')


if __name__ == '__main__':
    main()
