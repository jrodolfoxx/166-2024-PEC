f = int(input("Quantas fatias de pizza?: "))
a = int(input("quantos amigos ?: "))

divisão = f//a
resto= f%a

print(f'Cada amigo ganhará {divisão} pizzas e sobrará {resto}')
