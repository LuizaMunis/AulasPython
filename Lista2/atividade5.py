def quadrado(n):
  soma = 0
  for i in range(1, n + 1):
    soma += 2 * i - 1
  return soma

n = int(input("Digite um número natural: "))
print(f"O quadrado de {n} é: {quadrado(n)}")