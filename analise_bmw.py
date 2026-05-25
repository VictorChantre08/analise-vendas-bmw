import pandas as pd
import sqlite3

# --- PRIMEIRA PARTE: Tratamento de Dados ---

# 1. Carregar os dados
df = pd.read_csv('bmw_global_sales_dataset.csv')

# Ajustar o índice para começar em 1 em vez de 0
df.index = df.index + 1

# 2. Visualizar as primeiras linhas e informações básicas
print("--- DADOS ORIGINAIS ---")
print(df.head())

# 3. Tratamento de Dados
df = df.drop_duplicates()
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
df['total_revenue_usd'] = df['price_usd'] * df['units_sold']

# 4. Guardar o dataset limpo para o Power BI
df.to_csv('bmw_sales_cleaned.csv', index=False)
print("\nDados limpos e guardados com sucesso no ficheiro 'bmw_sales_cleaned.csv'!")


# --- SEGUNDA PARTE: Análise com SQL ---

# Criar uma ligação com uma base de dados em memória
conn = sqlite3.connect(':memory:')

# Enviar o DataFrame 'df' (que acabámos de limpar) para a base de dados SQL
df.to_sql('bmw_sales', conn, index=False, if_exists='replace')

# Escrever a Query SQL
query = """
    SELECT 
        country,
        model,
        SUM(units_sold) as total_units,
        SUM(total_revenue_usd) as total_revenue,
        AVG(price_usd) as avg_price
    FROM 
        bmw_sales
    GROUP BY 
        country, model
    ORDER BY 
        total_revenue DESC
    LIMIT 10;
"""

# Executar a query usando o pandas para visualizar facilmente
top_sales = pd.read_sql_query(query, conn)

# Ajustar o índice para começar em 1 em vez de 0
top_sales.index = top_sales.index + 1

print("\n--- TOP 10 VENDAS POR PAÍS E MODELO (SQL) ---")
print(top_sales)

# Fechar ligação
conn.close()