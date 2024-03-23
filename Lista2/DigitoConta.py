n1,n2,n3,n4=map(int,input('Digite os 4 numeros separados por espaço:').split())

s=n1+n2+n3+n4
digito= s%10

#transforma os numeros em string e concatena eles
formatados = ''.join(map(str, [n1, n2, n3, n4]))
conta = f"Conta: 00{formatados}-{digito}"

print(conta)