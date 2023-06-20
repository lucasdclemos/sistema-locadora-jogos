from estoque import *
from caixa import *
from usuario import *

def testa_modulo_usuario():
    # Teste para o cadastro de usuario novo
    if adiciona_usuario(1, "Lucas Lemos") == 1:
        print("OK -> teste de cadastrar usuario novo")
    else:
        print("ERRO -> teste de cadastrar usuario novo")
    # Teste para verificar se o usuario já cosnta no cadastro
    if verifica_usuario("Lucas Lemos") == 1:
        print("OK -> teste para verificar se usuário já consta")
    else:
        print("ERRO -> teste para verificar se usuário já consta")
    # Teste para quando se tenta adicionar id negativo
    if adiciona_usuario(-4, "Lucas Caúla") == -1:
        print("OK -> teste para a resposta quando se tenta adicionar id negativo")
    else:
        print("ERRO -> teste para a resposta quando se tenta adicionar id negativo")

testa_modulo_usuario() 