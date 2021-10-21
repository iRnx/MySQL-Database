import mysql.connector

# Conecta ao Banco de dados
mydb = mysql.connector.connect(
    host='localhost',
    user='root',  # root ou o usuário que você deseja logar #
    passwd='sua senha'
)

# Cria a Query, executa e salva registros no Banco de Dados
cursor = mydb.cursor()
cursor.execute('CREATE DATABASE python')

#  Para instalar o mysql connector: pip install mysql-connector-python #






