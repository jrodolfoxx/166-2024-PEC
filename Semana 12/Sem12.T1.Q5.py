def main():
    populacao_original = populacao = int(input("Digite a população de aves no início do ano 1600: ").strip())
    
    ano = 1599
    while True:
        num_nascimento = (1 / 100) * populacao
        num_mortes = (6 / 100) * populacao
        total_ano = (num_nascimento + populacao) - num_mortes
        ano += 1
        populacao = total_ano
        print(f"Ano: {ano}, Nascimentos: {round(num_nascimento)}, Mortes: {round(num_mortes)}, População por ano: {round(total_ano)}.".strip())
        if total_ano < ((10 /100) * populacao_original): break
    
if __name__=="__main__":
    main()
