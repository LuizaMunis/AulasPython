##Atividae 1
#Operações matemáticas

while True:
  n=[]

  for i in range(1,3):
    numero=int(input('Digite o %dº numero:'%i))
    n.append(numero)

  adicao= n[0]+n[1]
  subtracao= n[0] - n[1]
  multiplicacao= n[0]*n[1]
  divisao= n[0]/n[1]

  print('\n Adição:',adicao,'\n Subtração:',subtracao,'\n Multiplicação', multiplicacao,'\n Divisão', divisao)
  repetir=input('\nQuer repetir? ')
  if repetir!= "sim" :
    break
