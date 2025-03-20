def valida():
    while True:
        try:
#Entrada
            nota = float(input())
            if 0 <= nota <= 10:
                return nota
            else:
                print('Nota inválida.')
        except ValueError:
            print('Nota inválida.')


def conceito(nota):
    if nota >= 8.5:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 4.0:
        return "D"
    else:
        return "E"
    
def main():
#Processo
    nota = valida()
    resultado = conceito(nota)
#Saída
    print(f"O conceito é {resultado}")

if __name__ == '__main__':
    main()