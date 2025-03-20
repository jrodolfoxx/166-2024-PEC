def resposta():
    print("OPÇÕES: ")
    print("1 - SAUDAÇÃO")
    print("2 - BRONCA")
    print("3 - FELICITAÇÃO")
    print("0 - FIM")

     
def main():
    opcao = -1

    while opcao != 0:
        resposta()
#Entrada
        opcao = int(input())
#Processso e Saída
        if opcao == 1:
            print("1 - Olá. Como vai?")

        elif opcao == 2:
            print("2 - Vamos estudar mais.")

        elif opcao == 3:
            print("3 - Meus Parabéns!")
        elif opcao == 0:
            print("0 - Fim de serviço.")
        
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()

