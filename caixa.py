# Estrutura que representa o caixa da locadora
caixa_dict = dict(saldo = 0)
print(caixa_dict)

# Função para quando um usuário está alugando um jogo
def aluga_jogo():
    caixa_dict['saldo'] += 3
    return

# Função para quando a locadora quer comprar um novo jogo
def compra_jogo(valor):
    if caixa_dict['saldo'] < valor:
        print("A locadora não possui caixa suficiente para comprar esse jogo")
        return
    else:
        caixa_dict['saldo'] -= valor
        # Adicionar novo jogo no estoque
        print("Compra concluída com sucesso")
    return

aluga_jogo()
aluga_jogo()
aluga_jogo()
aluga_jogo()
print(caixa_dict)
compra_jogo(12)
print(caixa_dict)