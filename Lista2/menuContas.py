##Lista 2 Atividade 1

while True:
  n=[]

  print('1-Adição\n2-Subtração\n3-Divisão\n4-Multiplicação\n5-Sair')
  escolha=int(input('Escolha uma equação:'))

  for i in range(1,3):
      numero=int(input('Digite o %dº numero:'%i))
      n.append(numero)

  if(escolha ==1):
    adicao= n[0]+n[1]
    print(adicao)
  elif(escolha==2) :
    subtracao= n[0] - n[1]
    print(subtracao)
  elif(escolha==4):
   multiplicacao= n[0]*n[1]
   print(multiplicacao)
  elif(escolha==3) :
   divisao= n[0]/n[1]
   print(divisao)


  if escolha ==5 :
    break

