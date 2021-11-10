import os
import produtos
from datetime import datetime


def read_file(file: str):
    file = f"./comandas/{file}"
    f = open(file, "r")
    for position, line in enumerate(f):
        if(position == 6):
            products = [int(n) for n in line.split()]
            return products
    f.close()


now = datetime.now()
file_name = now.strftime("%d_%m_%Y")
file = os.path.join('.', 'relatorios', f'relatorio_{file_name}.txt')
f = open(file, "w+")
f.write(f'Relatorio do dia {now.strftime("%d/%m/%Y")}:\n')

orders = []
orders_report = []
price_orders = 0
qnt_orders = 0

for i in range(len(produtos.produtos)):
    orders_report.append([i, 0])

for root, dirs, files in os.walk("./comandas"):
    for filename in files:
        if(filename.endswith('.txt')):
            orders.append(read_file(filename))
    break  # Serve para ler somente o diretório atual

for i in orders:
    for j in i:
        qnt_orders += 1
        orders_report[j][1] += 1
        price_orders += produtos.produtos[j].get("price")
f.write(f'\nProdutos vendidos: \n')
f.write(f'Total: {qnt_orders}\n')
f.write(f'Total (preco): {price_orders}\n\n')

for i in orders_report:
    f.write(f'ID: {produtos.produtos[i[0]].get("id")}\n')
    f.write(f'Nome: {produtos.produtos[i[0]].get("name")}\n')
    f.write(f'Preco unitario: {produtos.produtos[i[0]].get("price")}\n')
    f.write(f'Quantidade vendida: {i[1]}\n')
    f.write(
        f'Quantidade ganha (preco): {produtos.produtos[i[0]].get("price") * i[1]}\n\n')

print(price_orders)
print(orders)
print(orders_report)
