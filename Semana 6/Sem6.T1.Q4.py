def number(h,i,j,k,l,):
    maior = max(h,i,j,k,l,)
    menor = min(h,i,j,k,l,)
    m = (h+i+j+k+l)/5
    return maior,menor,m

def main():
#Entrada
       a = int(input("Primeiro número: "))
       b = int(input("Segundo número: "))
       c = int(input("Terceiro número: "))
       d = int(input("Quarto número: "))
       e = int(input("Quinto número: "))
           
#Processo
       maior,menor,m = number(a,b,c,d,e,)

#Saída
       print(f'O maior deles é {maior}')
       print(f'O menor é {menor}')
       print(f'E a média entre eles é {m}') 
       
if __name__ =='__main__':
    main()
