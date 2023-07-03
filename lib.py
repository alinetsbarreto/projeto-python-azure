#Código que define as funções de limpar tela e tempo de permanência do que é exibido na tela.

import os #função do módulo os em Python que permite a execução de comandos no sistema operacional subjacente.
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # limpar a tela do terminal. Se o sistema operacional for Windows, executará "cls" para limpar a tela, se for outro sistema operacional (como Linux ou macOS), ele irá executar "clear".

def espera(segundos = 3):  #função para esperar 3 segundos a informação na tela
    time.sleep(segundos)

def mensagem(mensagem, segundos = 3):
    limpar_tela()   #função de limpar a tela
    print(mensagem) #imprimir msg definida quando utilizado essa função
    espera(segundos) #função de esperar 3 segundos
