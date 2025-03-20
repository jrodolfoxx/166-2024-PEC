def tempo():
#Processamento
    minuto = 60
    hora = 3600
    dia = 86400
    return minuto, hora, dia
     

def main():
#Entrada
      minuto, hora, dia = tempo()

      
#Saida
      print(minuto)
      print(hora)
      print(dia)

if __name__ == '__main__':
    main()