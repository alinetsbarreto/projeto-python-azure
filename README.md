# Python + Azure

## Descrição

- Projeto proposto no curso de Engenharia de Dados da Gama Academy;
- Utilizar a linguagem python para cadastrar informações de clientes e seus pedidos (produto) em um banco de dados na nuvem (Banco de Dados SQL do Microsoft Azure).

## Projeto
### Resumo
Os scripts elaborados garantem uma interação simplificada e eficiente com o banco de dados na nuvem, fornecendo recursos para cadastro, consulta e gerenciamento de informações de clientes e pedidos.
### Scripts Python
Os diferentes scripts Python que compõem o projeto são os seguintes:
- O script [lib.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/lib.py) define funções para limpar a tela e controlar o tempo de permanência das informações exibidas.
- O script [init.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/init.py) contém o código do menu, onde é possível selecionar as opções desejadas (Cadastro de clientes, Lista de clientes, Cadastro de pedidos, Lista de pedidos ou Sair). Esse código redireciona para as funções correspondentes.
- O script [funcoes_SQL.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/funcoes_SQL.py) estabelece a conexão com o Banco de Dados SQL fornecido pela plataforma Azure. Ele contém funções para cadastrar clientes e seus pedidos nas respectivas tabelas do banco de dados, além de permitir o acesso aos dados cadastrados quando necessário.
- O script [cadastro_cliente.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/cadastro_cliente.py) apresenta funcionalidades para cadastrar clientes, listar todos os dados dos clientes cadastrados no banco de dados e localizar clientes por meio de seu índice, utilizando as funções presentes no arquivo [funcoes_SQL.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/funcoes_SQL.py).
- O script [cadastro_pedido.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/cadastro_pedido.py) oferece a capacidade de cadastrar os pedidos dos clientes e listar todos os dados dos pedidos cadastrados no banco de dados, também utilizando as funções presentes no arquivo [funcoes_SQL.py](https://github.com/alinetsbarreto/exercicio-python-azure/blob/main/funcoes_SQL.py).

