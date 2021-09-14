#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#   No final, mostre uma listagem de preços, organizando os dados em forma tabular.


#fazer o len da palavra loja de roupas e dividir o valor por 2, para ficar centralizado
#após isso, somar  da metade do total de simbolos utilizados--> 60/2 + len('LOJA DE ROUPAS)/2 --> 37
print('='*60)
print(f'{"LOJA DE ROUPAS":>{37}}')
print('='*60)
produtos_precos=('camiseta',30,'camiseta floral',40,'camiseta social',50,'camisa regata',20,'moletom',90,'calça jeans',
                 60,'calça social',80,'cinto',40)
#para formatar, foi utilizado como valor total o número 60(referente ao print), menos o valor dos preços+o simbolo RS,totalizando 4 algarismos,resultando em 56 no total
#depois, foi reduzido pelo número de letras que cada produto continha
for c in range(0,len(produtos_precos),2):
    print(produtos_precos[c],end='.'*(56-len(produtos_precos[c])))
    print(f'R${produtos_precos[c+1]}')
print('='*60)
