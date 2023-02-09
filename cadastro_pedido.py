import lib
import funcoes_SQL 
import cadastro_cliente
import uuid

#Função para cadastrar pedido:
def cadastrar():
    lib.limpar_tela()

    cliente = funcoes_SQL.SQL_indice() #Função que localiza cliente pelo seu indice 

    pedido = {}
    pedido["id"] = str(uuid.uuid4())
    pedido["cliente_id"] = cliente ["id"]
    pedido["produto"] = input("Digite o nome do produto\n")
    pedido["quantidade"] = input("Digite a quantidade\n")
    pedido["valor"] = input("Digite o valor\n")
    pedido["valor_total"] = float(pedido["quantidade"]) * float(pedido["valor"])

    funcoes_SQL.SQL_pedidos(pedido)
    
    lib.mensagem("Pedido cadastrado com sucesso")

#Função que lista todos os pedidos cadastrado no banco de dados
def listar():
    lib.limpar_tela();
    funcoes_SQL.SQL_lerpedidos()
    input("Digite enter para continuar ...")
    lib.limpar_tela()
