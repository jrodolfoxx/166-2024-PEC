def ideal(altura,sexo):
    if sexo == 1:
        m = (72.7*altura)-58
        return m
    if sexo == 2:
        f = (62.1*altura)-44.7
        return f

def main():
#Entrada
    a = float(input("Digite a altura: "))
    s = int(input("E o gênero da pessoa, 1 para masculino e 2 para feminino: "))

#Processo
    resultado = ideal(a,s)

#Saída
    print(f'O peso ideal dessa pessoa é {resultado:.2f} kg')

if __name__ == '__main__':
    main()
    
    
