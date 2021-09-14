# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

 from random import randint
numeros=(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
maior_numero=menor_numero=numeros[0]
for numero in numeros:
    if numero>maior_numero:
        maior_numero=numero
    elif menor_numero>numero:
        menor_numero=numero
print(f'a tupla dos 5 valores aleatórios é:{numeros}')
print(f'o maior desses números  é o {maior_numero} e o menor é {menor_numero} ')
