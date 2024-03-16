def quadrado():
    nAsteriscos = 13
    for i in range(2):
        print('*' * nAsteriscos)
        if(i==1):
          break
        for j in range(5):
            nEspacos = 9
            print('*', ' ' * nEspacos, '*')

def losango(): 
    n = 6
    for i in range(1, n+1):
        print(' ' * (n - i) , '*' * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) , '*' * (2 * i - 1))


def seta():
    n=7
    es=6

    for i in range(1,4):
        print(' '*es,'* '*(i))
    for j in range(1,4):
        if( j ==2):
         print('* '*8)
        else:
         print('* '*n)
    for e in range(1,4):
     print(' '*es,'* '*(4-e))


print("Quadrado")
quadrado()
print("\nLosango")
losango()
print("\nSEta")
seta()   
