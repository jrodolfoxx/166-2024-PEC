x = float(input("Valor do raio: "))
PI = 3.141592

circunferencia = 2*PI*x
a_circulo = PI*x**2
a_esfera = 4*PI*x**2
vol_esfera = 4/3*PI*x**3

print(f'{circunferencia:.6f} o comprimento da circunferencia')
print(f'{a_circulo:.6f} a area do circulo')
print(f'{a_esfera:.6f} a area da esfera')
print(f'{vol_esfera:.6f} o volume da esfera')
