def numero():
    numeros = []
    for i in range(10, 1001, 10):
      numeros.append(str(i))

    sequencia = ", ".join(numeros)
    
    print(sequencia + ".")

      

if __name__ == '__main__':
   numero()