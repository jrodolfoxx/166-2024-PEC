def main():
    p1 = int(input("Digite a população do país A: "))
    p2 = int(input("Digite a população do país B: "))
    if p1 > p2: 
        populacao_a = p1
        populacao_b= p2
    elif p2 > p1: 
        populacao_a = p2
        populacao_b = p1
    
    anos = 0
    while True:
        taxa_n_a =((2 / 100) * populacao_a)
        taxa_n_b =((3 / 100) * populacao_b)
        populacao_a += round(taxa_n_a)
        populacao_b += round(taxa_n_b)
        anos += 1
        if populacao_b > populacao_a: break
    
    print(f"Levará {anos} anos até que a população ultrapasse a outra.")
if __name__=="__main__":
    main()