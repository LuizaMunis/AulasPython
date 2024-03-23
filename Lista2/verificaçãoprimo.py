##Lista 2 Atividade 2

n=int(input('Digite um numero:'))
for i in range (2,n):
  if(n %i ==0):
    print('nao é primo')
    break
  else:
    print('é primo')
    break
  
