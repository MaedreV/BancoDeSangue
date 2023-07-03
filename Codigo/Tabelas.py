import sqlite3

conexao = sqlite3.connect('BancoDeSangue.db')

# Cria um cursor para executar as consultas
cursor = conexao.cursor()

# Criação da tabela "Doadores"
tabela_doadores = """
CREATE TABLE Doadores (
  ID_do_doador INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(100),
  tipo_sanguineo VARCHAR(5),
  idade INT,
  genero VARCHAR(10),
  data_de_registro DATE,
  cidade VARCHAR(50),
  estado VARCHAR(50),
  pais VARCHAR(50)
)
"""

# Criação da tabela "Hospitais"
tabela_hospitais = """
CREATE TABLE Hospitais (
  ID_do_hospital INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_do_hospital VARCHAR(100),
  cidade VARCHAR(50),
  estado VARCHAR(50),
  pais VARCHAR(50)
)
"""

# Criação da tabela "Doacoes"
tabela_doacoes = """
CREATE TABLE Doacoes (
  ID_da_doacao INTEGER PRIMARY KEY ,
  ID_do_doador INTEGER,
  data_da_doacao DATE,
  local_da_doacao INT,
  quantidade_de_sangue DECIMAL(5, 2),
  FOREIGN KEY (ID_do_doador) REFERENCES Doadores(ID_do_doador),
  FOREIGN KEY (local_da_doacao) REFERENCES Hospitais(ID_do_hospital)
)
"""

# Executa as consultas para criar as tabelas
cursor.execute(tabela_doadores)
cursor.execute(tabela_hospitais)
cursor.execute(tabela_doacoes)

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()
