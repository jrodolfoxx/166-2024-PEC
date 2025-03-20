def fahrenheit(c):
     return (c * 9/5) + 32

def celsio(f):
     return (f - 32) * 5/9

def comaparacao(temp1, temp2):
     valor_1, escala_1 = temp1
     valor_2, escala_2 = temp2

     if escala_1 == escala_2:
        return temp1 if valor_1 > valor_2 else temp2
     
     else:
        if escala_2 == 'C':
            tcelsios_1 = valor_1
        else:
            tcelsios_1 = celsio(valor_1)

        if escala_2 == 'c':
            tcelsios_2 = valor_2
        else:
            tcelsios_2 = celsio(valor_2)
        
        if tcelsios_1 > tcelsios_2:
            maior_temp = (valor_1, escala_1)
        else:
            maior_temp = (valor_2, escala_2)

        return maior_temp


def formatar_temperatura(valor):
    if valor == int(valor):
        return f"{float(valor)}"  
    else:
        return f"{valor:.4f}".rstrip('0').rstrip('.')


def main():
     valor_1 = float(input())
     escala_1 = input().upper()[0]

     valor_2 = float(input())
     escala_2 = input().upper()[0]

     resultado = comaparacao((valor_1, escala_1), (valor_2, escala_2))
     valor_formatado = formatar_temperatura(resultado[0])

     print(f"({valor_formatado}, '{resultado[1]}')")

if __name__ == "__main__":
    main()