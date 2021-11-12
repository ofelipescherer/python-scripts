import os
from datetime import datetime
from produtos import produtos
from random import randint

now = datetime.now()
file_name = now.strftime("%H_%M")
file = os.path.join('.', 'comandas', f'comanda_{file_name}.txt')
f = open(file, "w+")

f.write('Resumo da comanda\n')
f.write(f'Hora: {now.strftime("%H:%M")}\nData: {now.strftime("%d/%m/%Y")}\n')
f.write('Cliente zzzzzzzzz\n\n')

qnt_escolhido = randint(1, 4)
prod_escolhidos = []
prod_id = []

# qnt_escolhido_bebidas = randint(1, 4)
# bebi_escolhidas = []
# bebi_id = []

for i in range(qnt_escolhido):
    prod = randint(0, len(produtos)-1)
    prod_escolhidos.append(
        produtos[prod])
    prod_id.append(prod)

# for i in range(qnt_escolhido_bebidas):
#     bebida = randint(0, len(produtos.bebidas)-1)
#     bebi_escolhidas.append(
#         produtos.bebidas[bebida])
#     bebi_id.append(bebida)

f.write('Ids produtos:\n')
for i in prod_id:
    f.write(f'{i} '),

f.write('\n')

# f.write('Ids bebidas:\n')
# for i in bebi_id:
#     f.write(f'{i} '),

f.write('\n')

f.write('Relatorio\n\n')
f.write('Produtos\n')
for i in prod_escolhidos:
    f.write(f'Id: {i.get("id")}\n')
    f.write(f'Nome: {i.get("name")}\n')
    f.write(f'Preco: {i.get("price")}\n\n')

# f.write('Bebidas\n')
# for i in bebi_escolhidas:
#     f.write(f'Id: {i.get("id")}\n')
#     f.write(f'Nome: {i.get("name")}\n')
#     f.write(f'Preco: {i.get("price")}\n\n')


f.close()
