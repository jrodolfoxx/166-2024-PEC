def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    
    return sequencia

def main():
#Entrada
    n = int(input("Digite um número para a sequência de Fibonacci: "))

#Processo
    if n >= 2:
        fib_sequecia = fibonacci(n)
        print(', '.join(map(str, fib_sequecia)))

    else:
        print("O valor n deve ser maior que 2.")

if __name__ == '__main__':
    main()
