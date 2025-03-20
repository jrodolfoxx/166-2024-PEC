#Entrada
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

#Processo
a = anos*365
m = meses*30

#Saída
print(f'Sua ideda expressa em dias: {a+m+dias} dias')
