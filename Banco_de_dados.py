# Biblioteca responsavel por interagir com o banco de dados
import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect('Balanco_de_caixa.db')

# Criar um objeto cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela de categorias
cursor.execute('''
CREATE TABLE IF NOT EXISTS Registro_de_vendas (
    data_do_balanco DATE AUTO INCREMENT,
    balanco_do_dia DECIMAL NOT NULL,
    dalanco_do_mes DECIMAL NOT NULL
);
''')

# Salvar as alterações
conexao.commit()
conexao.close()