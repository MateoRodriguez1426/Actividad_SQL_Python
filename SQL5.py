import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="midb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE pedidos (IdPedido VARCHAR(25), NombrePedidos VARCHAR(35))")