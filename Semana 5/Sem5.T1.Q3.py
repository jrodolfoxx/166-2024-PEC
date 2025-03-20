def percentual(preco,valor_p):
    a = preco*(1+valor_p/100)
    d = preco*(1-valor_p/100)
    return a, d

def main():
#Entrada
    preco = float(input("Digite o preço: "))
    valor_p = float(input("O valor percentual: "))

#Processo
    a,d = percentual(preco,valor_p)

#Saída
    print(f'O preço com aumento será R$ {a:.2f}')
    print(f'O preço em desconto será R$ {d:.2f}')

if __name__ == '__main__':
    main()
    
