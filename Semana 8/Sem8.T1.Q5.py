def massa(peso,altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        return imc,'Abaixo do peso'
    if 18.5 < imc < 25:
        return imc,'Peso normal'
    if 25 < imc < 30:
        return imc,'Sobrepeso'
    if 30 < imc < 35:
        return imc,'Obeso leve'
    if 35 < imc < 40:
        return imc,'Obeso moderado'
    if 40 <= imc:
        return imc,'Obeso mórbido'

def main():
#Entrada
    p = float(input("Digite o peso em Kg: "))
    a = float(input("Digite a altura em M: "))

#Processo
    imc,resultado = massa(p,a)

#Saída
    print(f'O índice de massa corporal(IMC) dessa pessoa é {imc:.2f}')
    print(f'Classificada como {resultado}')

if __name__ == '__main__':
    main()
    
