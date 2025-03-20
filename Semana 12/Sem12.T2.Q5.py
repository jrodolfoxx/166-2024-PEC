def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primos_no_intervalo(x, y):
    primos = []
    for num in range(x, y + 1):
        if eh_primo(num):
            primos.append(num)
    return primos


def main():
    try:
        x = int(input("Digite o primeiro valor inteiro: "))
        y = int(input("Digite o segungo valor inteiro: "))
        
        if x > y:
            print("O valor de x deve ser menor ou igual ao valor de y.")
        else:
            primos = primos_no_intervalo(x, y)
            if primos:
                for primo in primos:
                     print(f'{primo}')
            else:
                print("Não há números primos entre", x, "e", y, ".")
    except ValueError:
        print("Por favor, digite números inteiros válidos.")



if __name__ == "__main__":
    main()

