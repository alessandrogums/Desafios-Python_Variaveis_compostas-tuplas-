# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times_brasileirao=('Atlético-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Atletico-PR','Atletico-GO',
                   'Ceara','Internacional','Santos','Corinthians','Juventude','Bahia','Sao Paulo','Fluminense','Cuiaba',
                   'Sport','America-MG','Gremio','Chapecoense')
print(f'dos {len(times_brasileirao)} times do brasileirão:')
print(f'os 5 primeiros times do brasileirão são:{times_brasileirao[0:5]}')
print(f'os 4 últimos colocados são:{times_brasileirao[-4:]}')
print(f'os times em ordem alfabética ficam:{sorted(times_brasileirao)}')
print(f'o chapecoense está na {times_brasileirao.index("Chapecoense")+1}º posição')
