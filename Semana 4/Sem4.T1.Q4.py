hora = int(input("Hora: "))
minuto = int(input("Minutos: "))
segundos = int(input("Segundos: "))

s = hora*3600
m = minuto*60

print(f'Se passaram ao todo {s+m+segundos} segundos')
