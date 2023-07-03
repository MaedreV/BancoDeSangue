import sqlite3

conexao = sqlite3.connect('BancoDeSangue.db')

# Cria um cursor para executar as consultas
cursor = conexao.cursor()

# Popula a tabela "Doadores"
popula_doadores = """
INSERT INTO Doadores (nome, tipo_sanguineo, idade, genero, data_de_registro, cidade, estado, pais)
VALUES
    ('Raul', 'A+', 19, 'Masculino', '2022-01-01', 'Recife', 'Pernambuco', 'Brasil'),
    ('Ingrid', 'B-', 18, 'Feminino', '2022-02-02', 'Recife', 'Pernambuco', 'Brasil'),
    ('Samuel', 'O+', 31, 'Masculino', '2022-03-03', 'Recife', 'Pernambuco', 'Brasil'),
    ('Melissa', 'A-', 26, 'Feminino', '2023-06-07', 'São Paulo', 'São Paulo', 'Brasil'),
    ('Alfredo', 'O-', 29, 'Masculino', '2023-08-11', 'São Paulo', 'São paulo', 'Brasil'),
    ('Luisa', 'B+', 29, 'Feminino', '2023-08-11', 'São Paulo', 'São paulo', 'Brasil');
"""

cursor.execute(popula_doadores)

# Popula a tabela "Hospitais"
popula_hospitais = """
INSERT INTO Hospitais (nome_do_hospital, cidade, estado, pais)
VALUES
    ('Hospital Português', 'Recife', 'Pernambuco', 'Brasil'),
    ('Santa Joana', 'Recife', 'Pernambuco', 'Brasil'),
    ('Hospital São Lucas', 'São Paulo', 'São Paulo', 'Brasil'),
    ('Hospital Albert Einstein', 'São Paulo', 'São Paulo', 'Brasil')
"""
cursor.execute(popula_hospitais)

popula_doacoes = """
INSERT INTO doacoes (ID_do_doador, data_da_doacao, local_da_doacao, quantidade_de_sangue)
VALUES (1, '2023-05-05', 1, 450),
(2, '2023-04-20', 2, 300),
(3, '2023-06-09', 2, 600),
(4, '2023-08-15', 3, 450),
(5, '2023-10-12', 4, 400),
(6, '2023-11-28', 3, 350);
"""

cursor.execute(popula_doacoes)

conexao.commit()

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()