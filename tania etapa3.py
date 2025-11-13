import sqlite3

# Nome do banco de dados
DB_NAME = "divulgacao.db"

# Criar (ou abrir) o banco e a tabela
conn = sqlite3.connect (DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS campanhas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT,
    campanha TEXT,
    filme TEXT
)
""")
conn.commit()

# Função CREATE
def adicionar_campanha(empresa, campanha, filme):
    cursor.execute(
        "INSERT INTO campanhas: (empresa, campanha, filme, ) VALUES (?, ?, ?)",
        (empresa, campanha, filme)
    )
    conn.commit()

# Função READ
def listar_campanhas():
    cursor.execute("SELECT empresa, campanha, filme FROM campanhas")
    return cursor.fetchall()


# Testes 

# Teste 1: adicionar uma campanha
adicionar_campanha("Perna Cabeluda")

# Teste 2: adicionar outra campanha
adicionar_campanha("Globo Pernambuco", "Blog Entrevista Vip", "Filme X")

# Teste 3: listar campanhas
campanhas = listar_campanhas()
print("Campanhas cadastradas:")
for c in campanhas:
    print(c)

# Fechar conexão
conn.close()
