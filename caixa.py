from estoque import adiciona_jogo_catalogo, estoque_dict
from arquivo import arquivo_caixa, salva_dados

caixa_dict = {"saldo":0}

def recupera_dados_caixa():
  caixa_dict.clear()
  dados = arquivo_caixa()
  if dados != {}:
    caixa_dict.update(arquivo_caixa())
  else:
    caixa_dict.update({"saldo": 0})
  # print(caixa_dict)
  return

def salva_dados_caixa():
  salva_dados("arquivos/caixa.json", caixa_dict)
  return
  
# Função para quando um usuário está alugando um jogo
def aluga_jogo():
  caixa_dict['saldo'] += 3
  # print("O aluguel foi concluído com sucesso. O caixa da loja agora é " + str(caixa_dict['saldo']))
  return 1

# Função para quando a locadora quer comprar um novo jogo
def compra_jogo(nome, valor):
  if int(caixa_dict['saldo']) < valor and valor > 0:
    return -2
  else:
    caixa_dict['saldo'] -= valor
    adiciona_jogo_catalogo(nome, 1)
    return -1
