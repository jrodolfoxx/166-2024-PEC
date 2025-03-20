d = int(input("Quantos km até esse planeta?: "))
v = int(input("Qual a velocidade da nossa nave?: "))

h = d//v

print(f'Levará {h//24} dias e {h%24} horas')
