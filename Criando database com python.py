import mysql.connector

# Conecta ao Banco de dados
mydb = mysql.connector.connect(
    host='localhost',
    user='root',  # root ou o usuário que você deseja logar #
    passwd='sua senha'
)

cursor = mydb.cursor()
cursor.execute('CREATE DATABASE python') # Cria o Banco de dados #

#  Para instalar o mysql connector: pip install mysql-connector-python #






