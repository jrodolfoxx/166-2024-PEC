def promocao(x):
    d = x*0.91
    p = x/5
    v = (x*1.17)/10
    return d,p,v

def main():
#Entrada
    preco = float(input("Valor da compra: "))

#Processo
    d,p,v = promocao(preco)

#Saída
    print(f'Pagamento a vista:R$ {d:.2f}')
    print(f'Parcelado em 5 vezes:Cada parcela R$ {p:.2f}')
    print(f'Parcelado em 10 vezes:Cada parcela R$ {v:.2f}')

if __name__ =='__main__':
    main()
