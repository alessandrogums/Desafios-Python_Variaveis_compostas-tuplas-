#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
print(len(numeros))
numero=int(input('digite um número de 0 a 10:'))
while numero>10 or numero<0:
    print('digitou um número errado')
    numero=int(input('digite um número entre 0 a 10 novamente:'))
print(f'você digitou o número {numeros[numero]}')
