
segundos = int(input("Digite a quantidade de segundos: "))
dias = segundos // (24 * 3600)
restoSegundos = segundos % (24 * 3600)
horas = restoSegundos // 3600
restoSegundos %= 3600
minutos = restoSegundos // 60
restoSegundos %= 60
segundos_final = restoSegundos

print("Dias:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_final)