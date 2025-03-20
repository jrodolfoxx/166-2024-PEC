#Entrada
altura = int(input("Altura da sala: "))
comprimento = int(input("Comprimento da sala: "))
largura = int(input("Largura da sala: "))

#processo
a_piso =  largura*comprimento
v_sala =  largura*comprimento*altura
a_parede =  2*altura*largura+ 2*altura*comprimento

#saída
print(f'A área do piso da sala é {a_piso} metros quadrados')
print(f'O volume da sala é {v_sala} metros cubicos')
print(f'E a área da parede é {a_parede} metros quadrados')
