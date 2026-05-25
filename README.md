# 🚗 Análise Global de Vendas - BMW

## 📌 Visão Geral
Projeto de Análise de Dados focado no pipeline de vendas globais da BMW. O objetivo principal do projeto foi realizar a extração, o tratamento e a análise de faturamento utilizando Python e SQL, gerando uma base limpa e estruturada pronta para consumo no Power BI.

## 🛠️ Tecnologias Utilizadas
* **Python (Pandas):** Limpeza, formatação de datas, remoção de duplicatas e cálculo de faturamento (ETL).
* **SQLite3:** Banco de dados em memória para execução de queries relacionais.
* **SQL:** Agrupamento e ordenação de dados de vendas.

## ⚙️ Arquitetura do Código
1. **Tratamento de Dados:**
   - Leitura da base original `bmw_global_sales_dataset.csv`.
   - Conversão das colunas de ano e mês para formato `datetime`.
   - Criação da métrica de Faturamento Total (`total_revenue_usd`) multiplicando o preço pelas unidades vendidas.
   - Exportação da base tratada para `bmw_sales_cleaned.csv`.
2. **Análise de Negócio:**
   - Criação de conexão em memória com `sqlite3`.
   - Construção de query SQL agregando unidades vendidas, faturamento total e preço médio por País e Modelo.
   - Extração do **Top 10 Vendas** focado em maior faturamento.

## 🚀 Como Executar
1. Clone este repositório.
2. Certifique-se de ter a biblioteca `pandas` instalada (`pip install pandas`).
3. Adicione o arquivo de dados original `bmw_global_sales_dataset.csv` na raiz do projeto.
4. Execute o script principal: `python etl_bmw_sales.py`.
5. O terminal exibirá o Top 10 de vendas por país e modelo, e o arquivo limpo será gerado automaticamente.
