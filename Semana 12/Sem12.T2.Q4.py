def primo(x):
    if x <= 1:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        
    return True

def main():
    numero = int(input("Digite um número para saber se ele é primo: "))

    if primo(numero):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    main()