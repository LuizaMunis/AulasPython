proximo = 1
anterior = 0

n1 = int(input("Quantos termos quer ver: "))
    
print("\n0 ", end='')
n1 -= 1
    
while n1:
    print(f"{proximo} ", end='')
    atual = proximo
    proximo += anterior
    anterior = atual
    n1 -= 1
