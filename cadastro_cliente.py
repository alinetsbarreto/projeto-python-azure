import lib
import funcoes_SQL 
import uuid  #biblioteca python que ajuda a gerar objetos aleatórios de 128 bits como ids.

#Função para cadastrar cliente:
def cadastrar():
    lib.limpar_tela()
   
    cliente = {}
    cliente["id"] = str(uuid.uuid4())
    cliente["nome"] = input("Digite o nome do cliente\n")
    cliente["telefone"] = input("Digite o telefone do cliente\n")
    cliente["email"] = input("Digite o email do cliente\n")
  
    funcoes_SQL.SQL_clientes(cliente)
    
    lib.mensagem("Cliente cadastrado com sucesso")

#Função que lista todos os dados do cliente cadastrado no banco de dados
def listar():
    lib.limpar_tela();
    
    funcoes_SQL.SQL_lerclientes()
    input("Digite enter para continuar ...")
    
    lib.limpar_tela()

#Função que localiza cliente pelo seu indice
def localiza_cliente():
    lib.limpar_tela()
    funcoes_SQL.SQL_indice()



