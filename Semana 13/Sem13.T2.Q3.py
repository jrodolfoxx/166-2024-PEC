def main():
    lista = []
    aprovados = []

    print("Digite a nota de 50 alunos:")
    for i in range(50):
        while True:
            nota = float(input(f'{i+1} nota: '))
            if 0 <= nota <= 10:
               lista.append(nota)
               break
            else:
                print("Nota Inválida")

    for i, nota in enumerate(lista):
        if nota >= 6:
            aprovados.append(i)

    print(f'As notas maiores que 6 foram:')
    print(aprovados)

if __name__ == "__main__":
    main()
