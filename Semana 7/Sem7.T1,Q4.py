def mensagem(x):
    if x.lower() in 'aeiou':
        return 'vogal'
    elif x.lower() in 'bcdfghijklmnpqrstvwxyz':
        return 'consoante'
    elif x.lower() in '0123456789':
        return 'número'
    else:
        return 'símbolo'


def main():
#entrada
  caractere = input("Digite uma caractere aleatória: ")
   
#processo
  resultado = mensagem(caractere)

#saída
  print(f'Ela é {resultado}.')

if __name__ == '__main__':
    main()
