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

def testa_modulo_estoque():
    adiciona_jogo_catalogo("Jogo1", 1)
    adiciona_jogo_catalogo("Jogo2", 0)
    # Teste para verificar que um jogo consta no estoque
    if verifica_estoque("Jogo1") > 0:
        print("OK -> teste de jogo presente no estoque e com exemplares")
    else:
        print("ERRO -> teste de jogo presente no estoque e com exemplares")
    # Teste para verificar que um jogo consta no estoque, mas sem exemplares
    if verifica_estoque("Jogo2") == 0:
        print("OK -> teste de jogo presente no estoque sem exemplares")
    else:
        print("ERRO -> teste de jogo presente no estoque sem exemplares")
    # Teste para verificar que um jogo não consta no estoque
    if verifica_estoque("Jogo3") == -1:
        print("OK -> teste de jogo que não consta no estoque")
    else:
        print("ERRO -> teste de jogo que não consta no estoque")               
    # Teste para cadastrar um jogo alugado, relacionando com um usuário
    if cadastrar_jogo_alugado("Jogo1", 1) == 1:
        print("OK -> teste para cadastrar jogo alugado")
    else:
        print("ERRO -> teste para cadastrar jogo alugado")

def testa_modulo_caixa():
    aluga_jogo()
    aluga_jogo()
    # Teste para verificar se o saldo aumenta com o aluguel de um jeito
    if aluga_jogo() == 1:
        print("OK -> teste para verificar o caixa após o aluguel de um jogo")
    else:
        print("ERRO -> teste para verificar o caixa após o aluguel de um jogo")
    # Teste para a compra de um jogo com sucesso
    if compra_jogo("Jogo5", 3) == -1:
        print("OK -> Teste para o caixa com a compra de um jogo novo")
    else:
        print("ERRO -> Teste para o caixa com a compra de um jogo novo")
    # Teste para a compra de um jogo sem saldo suficiente
    if compra_jogo("Jogo5", 100) == -2:
        print("OK -> Teste para o caixa com a compra de um jogo novo, mas sem saldo suficiente")
    else:
        print("ERRO -> Teste para o caixa com a compra de um jogo novo, mas sem saldo suficiente")

print("Testes módulo usuário")
testa_modulo_usuario() 
print("Testes módulo estoque")
testa_modulo_estoque()
print("Testes módulo caixa")
testa_modulo_caixa()