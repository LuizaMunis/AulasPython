cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0

umReal = 0
cinquentaCentavos = 0
vinteCincoCentavos = 0
dezCentavos = 0
cincoCentavos = 0
umCentavo = 0

valor = float(input('Digite um valor: '))


if valor >= 100:
    cem = int(valor / 100)
    valor -= cem * 100

if valor >= 50:
    cinquenta = int(valor / 50)
    valor -= cinquenta * 50

if valor >= 20:
    vinte = int(valor / 20)
    valor -= vinte * 20

if valor >= 10:
    dez = int(valor / 10)
    valor -= dez * 10

if valor >= 5:
    cinco = int(valor / 5)
    valor -= cinco * 5

if valor >= 2:
    dois = int(valor / 2)
    valor -= dois * 2


if valor >= 1:
    umReal = int(valor / 1)
    valor -= umReal * 1

if valor >= 0.5:
    cinquentaCentavos = int(valor /0.5)
    valor -= cinquentaCentavos * 0.5

if valor >= 0.25:
    vinteCincoCentavos = int(valor / 0.25)
    valor -= vinteCincoCentavos * 0.25

if valor >= 0.10:
    dezCentavos = int(valor / 0.10)
    valor -= dezCentavos * 0.10

if valor >= 0.05:
    cincoCentavos = int(valor / 0.05)
    valor -= cincoCentavos * 0.05

if valor >= 0.01:
    umCentavo = int(valor / 0.01)
    valor -= umCentavo * 0.01

print('Notas:')
print(f'{cem} nota(s) de R$100.00')
print(f'{cinquenta} nota(s) de R$50.00')
print(f'{vinte} nota(s) de R$20.00')
print(f'{dez} nota(s) de R$10.00')
print(f'{cinco} nota(s) de R$5.00')
print(f'{dois} nota(s) de R$2.00')

print('Moedas:')
print(f'{umReal} moeda(s) de R$1.00')
print(f'{cinquentaCentavos} moeda(s) de R$0.50')
print(f'{vinteCincoCentavos} moeda(s) de R$0.25')
print(f'{dezCentavos} moeda(s) de R$0.10')
print(f'{cincoCentavos} moeda(s) de R$0.05')
print(f'{umCentavo} moeda(s) de R$0.01')
