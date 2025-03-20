def escola(x,y,z,m):
    final = (x + y * 2 + z * 3 + m)/7
    if 9.0 <= final:
        return final,'A','Aprovado'
    if 7.5 <= final < 9.0:
        return final,'B','Aprovado'
    if 6.0 <= final < 7.5:
        return final,'C','Aprovado'
    if 4.0 <= final < 6.0:
        return final,'D','Reprovado'
    if final < 4.0:
        return final,'E','Reprovado'

def main():
#Entrada
    matricula = input("Digite a matricula: ")
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("E Terceira nota: "))
    media = float(input("Média de exercícios: "))

#Processo
    final,valor,resultado = escola(n1,n2,n3,media)

#Saída
    print(f'A matricula do aluno: {matricula}')
    print(f'Sua média final: {final:.2f}')
    print(f'Conceito: {valor}')
    print(f'O aluno está {resultado}')

if __name__ == '__main__':
    main()
