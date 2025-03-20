#Entrada
x = float(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

#Processo
soma = x+y
mult = x*y
divi = x/y
d_inteira = x//y
expo = x**y
modulo = x%y

#Saída
print(f'Soma: {soma}')
print(f'Concatenação de strings: {x}{y}')
print(f'Multiplicação: {mult}')
print(f'{x}'*y)
print(f'Divisão: {divi}')
print(f'Divisão inteira: {d_inteira}')
print(f'Exponenciação: {expo}')
print(f'Módulo: {modulo}')
