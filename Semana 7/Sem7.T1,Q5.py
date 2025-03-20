def nota(x,y,z):
    media = (x+y+z)/3
    if z>8:
        media += 1
    if media >10:
        media = 10
        
    return media
    

def main():
#entrada
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("E Terceira nota: "))
   
#processo
    media = nota(n1,n2,n3) 

#saída
    print(f'A média das 3 notas é {media:.2f}.')

if __name__ == '__main__':
    main()
