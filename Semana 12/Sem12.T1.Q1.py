def corrida(x):
    tartaruga = 1
    lebre = 10
    diferença = lebre - tartaruga
    tempo = x/diferença
    return tempo



def main():
#Entrada
    distancia = int(input("Quantos metros a tartaruga sai na frente da lebre: "))

#Processo
    resultado = corrida(distancia)

#Saída
    print(f'Levará {resultado:.0f} minutos até que a lebre alcance a tartaruga.')

if __name__ == '__main__':
    main()