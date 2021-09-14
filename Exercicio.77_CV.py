# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras=('bola','sapato','cadeira','raquete','camarao','godzilla')
vogais=('aeiou')
x='jardim'
cont=0
for c in range(0,len(palavras)):
    print(f'\na palavra {palavras[c]} tem vogais:',end=' ')
    cont = 0
    while len(palavras[c])-1>=cont:
        if palavras[c][cont] in 'aeiou':
            print(palavras[c][cont],end=' ')
        cont+=1

