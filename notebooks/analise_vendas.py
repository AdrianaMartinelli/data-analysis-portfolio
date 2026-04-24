import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregar dados
df = pd.read_csv('../datasets/vendas.csv')

# criar coluna de faturamento
df['faturamento'] = df['preco'] * df['quantidade']

# visualizar dados
print(df.head())

# faturamento por produto
faturamento_produto = df.groupby('produto')['faturamento'].sum().sort_values(ascending=False)

print(faturamento_produto)

# gráfico
plt.figure(figsize=(8,5))
sns.barplot(x=faturamento_produto.index, y=faturamento_produto.values)
plt.xticks(rotation=45)
plt.title('Faturamento por Produto')

plt.savefig('../images/grafico_vendas.png')
plt.show()