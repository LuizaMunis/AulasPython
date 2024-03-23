primos=[]

n = int(input('Digite um número: '))

for numero  in range(2   , n + 1):
    for i in range(2, numero):
        if numero  % i == 0:
            break
    else: primos.append(numero)

print(primos) 