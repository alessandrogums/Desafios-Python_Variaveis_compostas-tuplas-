# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

n1=int(input('digite o primeiro valor:'))
n2=int(input('digite o segundo valor:'))
n3=int(input('digite o terceiro valor:'))
n4=int(input('digite o quarto valor:'))
numeros=(n1,n2,n3,n4)
print(f'o número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'o número 3 apareceu primeiramente na posição {numeros.index(3)+1}')
else:
    print('o valor 3 não foi digitado!')
print('os números pares são:',end='')
qte_pares=0
for numero in numeros:
    if numero % 2 ==0:
        print(f'{numero}',end=' ')
        qte_pares+=1
if qte_pares==0:
    print('0 números pares')
