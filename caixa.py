from estoque import adiciona_jogo_catalogo, estoque_dict

# Estrutura que representa o caixa da locadora
caixa_dict = dict(saldo = 0)

# Função para quando um usuário está alugando um jogo
def aluga_jogo():
    caixa_dict['saldo'] += 3
    return

# Função para quando a locadora quer comprar um novo jogo
def compra_jogo(valor, nome):
    if caixa_dict['saldo'] < valor:
        print("Caixa não suficiente para comprar esse jogo")
        return
    else:
        caixa_dict['saldo'] -= valor
        adiciona_jogo_catalogo(nome)
        print("Compra concluída com sucesso")
    return

aluga_jogo()
aluga_jogo()
aluga_jogo()
aluga_jogo()
compra_jogo(5, "Jogo da Vida")
print(estoque_dict)