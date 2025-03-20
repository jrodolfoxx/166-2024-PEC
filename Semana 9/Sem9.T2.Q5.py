def resposta(a,b,c,d,e):
   positivas = [a,b,c,d,e]
   num = positivas.count("S")

   if num == 5: 
      return ("Assassino")
   elif num in [3,4]:
      return ("Cúmplice")
   elif num == 2:
      return ("Suspeito")
   else:
      return("Inocente")


def main():
#Entrada
   print("Ocorreu um crime grave, responda as perguntas a investiação.")
   print("Telefonou para a vítima ?")
   r1 = input("Responda com 'S' ou 'N': ").upper().strip()

   print("Esteve no local do crime ?")
   r2 = input("Responda com 'S' ou 'N': ").upper().strip()

   print("Mora perto da vítima ?")
   r3 = input("Responda com 'S' ou 'N': ").upper().strip()

   print("Devia para a vítima ?")
   r4 = input("Responda com 'S' ou 'N': ").upper().strip()

   print("Já trabalhou com a vítima ?")
   r5 = input("Responda com 'S' ou 'N': ").upper().strip()

#Processo
   veredito = resposta(r1,r2,r3,r4,r5)

#Saída
   print(f'Declarado {veredito}.')

if __name__ == '__main__':
   main()
   