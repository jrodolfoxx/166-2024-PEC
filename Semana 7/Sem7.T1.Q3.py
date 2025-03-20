def semaforo(cor):
    if cor.upper() == 'V':
        return 'Siguir'
    elif cor.upper() == 'A':
        return 'Ter Atenção'
    elif cor.upper() == 'E':
        return 'Parar'
    

def main():
#entrada
  sinal = input("Digite 'V'(verde),'A'(Amarelo) ou 'E'(vermelho): ")
   
#processo
  resultado = semaforo(sinal)

#saída
  print(f'Então você deve {resultado}.')


if __name__ == '__main__':
    main()
