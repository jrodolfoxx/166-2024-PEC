def parcelas():
    valor = float(input())

    for i in range(1, 25):
        p = valor/i
        print(f'{i}x de R$ {p:.2f}')
    

def main():
    parcelas()


if __name__ == '__main__':
    main()