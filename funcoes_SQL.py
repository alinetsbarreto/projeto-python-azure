import pyodbc
import lib

#Conectar com SQL server
conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql-aline-datalake.database.windows.net,1433;Database=aline-dadoscsv;Uid=administrador;Pwd=JAh12A4r;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
cursor = conn.cursor()   

#Função para cadastrar clientes na tabela "clientes" do banco de dados
def SQL_clientes(d):
    cursor.execute("INSERT INTO clientes (id, nome, telefone, email) VALUES (?, ?, ?, ?)", (d['id'], d['nome'], d['telefone'],d['email']))
    cursor.commit()
    
#Função para cadastrar pedidos na tabela "pedidos" do banco de dados
def SQL_pedidos(d):
    cursor.execute("INSERT INTO pedidos (id, cliente_id, produto, quantidade, valor, valor_total) VALUES (?, ?, ?, ?, ?, ?)", (d['id'], d['cliente_id'], d['produto'], d['quantidade'], d['valor'], d['valor_total']))   
    cursor.commit()


#Função para exibir clientes que estão na tabela "clientes" do banco de dados
def SQL_lerclientes():
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    print("-" * 60)
    for item in rows:
        print("Id: " , item[0])
        print("Nome: " , item[1])
        print("Telefone: " , item[2])
        print("Email: " , item[3])
        print("-" * 60)

#Função para exibir pedidos que estão na tabela "pedidos" do banco de dados
def SQL_lerpedidos():
    cursor.execute("SELECT * FROM pedidos")
    rows = cursor.fetchall()
    print("-" * 60)
    for item in rows:
        print("Id: " , item[0])
        print("Cliente_id: ", item[1])
        print("Produto: ", item[2])
        print("Quantidade: ", item[3])
        print("Valor da unidade: R$", item[4])
        print("Valor Total: R$", item[5])
        print("-" * 60)

#Função para exibir clientes por ID e selecionar qual cliente será retornado no final da função
def SQL_indice():
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    for i, item in enumerate(rows):
        print("Indice: " + str(i+ 1))
        print("Nome: " , item[1])
        print("Telefone: " , item[2])
        print("Email: " , item[3])
        print("-" * 60)
  
    while True:
        try:
            indice = int(input("Digite o indice de qual cliente você deseja selecionar:\n"))
            if indice < 1 or indice > len(rows):
                raise ValueError
            break
        except ValueError:
            lib.mensagem("opção inválida")
            SQL_indice()

    row = rows[(indice -1)]
    cliente = {
        "id": row[0],
        "nome": row[1],
        "telefone": row[2],
        "email": row[3],
    }
    return cliente
