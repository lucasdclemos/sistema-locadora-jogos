from arquivo import monta_arquivo_solicitacao, resposta_fornecedor, arquivo_estoque, arquivo_jogos_alugados, salva_dados

estoque_dict = {}
jogos_alugados_dict = {}

def salva_dados_jogos_alugados():
  salva_dados("arquivos/jogos_alugados.json", jogos_alugados_dict)
  return

def salva_dados_estoque():
  salva_dados("arquivos/estoque.json", estoque_dict)
  return

def recupera_estoque():
  estoque_dict.update(arquivo_estoque())
  return

def recupera_jogos_alugados():
  jogos_alugados_dict.update(arquivo_jogos_alugados())
  return

def adiciona_jogo_catalogo(nome, quantidade):
  novo_id = len(estoque_dict) + 1
  dict_auxiliar = dict(nome = nome, quantidade = quantidade)
  estoque_dict.update({novo_id: dict_auxiliar})
  return

def cadastrar_jogo_alugado(nome, usuario_id):
  auxiliar = verifica_estoque(nome)
  if int(auxiliar) > 0:
    dict_auxiliar = dict(jogo = nome)
    jogos_alugados_dict.update({usuario_id: dict_auxiliar})
    estoque_dict[auxiliar]['quantidade'] -= 1
    return aluga_jogo()
  elif auxiliar == 0:
    print("Não há exemplares do jogo em estoque.")
    monta_arquivo_solicitacao({"jogos":[{"nome": nome, "quantidade": 1}]})
    print("A soliticação do jogo já foi enviada para o fornecedor.")
    valor = resposta_fornecedor(nome)
    return compra_jogo(nome, valor)
  else:
    print("O jogo não existe no estoque")
    monta_arquivo_solicitacao({"jogos":[{"nome": nome, "quantidade": 1}]})
    print("A soliticação do jogo já foi enviada para o fornecedor.")
    valor = resposta_fornecedor(nome)
    return compra_jogo(nome, valor)
  # print(jogos_alugados_dict)
  return 0

def verifica_estoque(nome):
  for jogo in estoque_dict:
    if estoque_dict[jogo]["nome"] == nome:
      if estoque_dict[jogo]['quantidade'] > 0:
        return jogo
      else:
        return 0
  return -1


from caixa import compra_jogo, aluga_jogo
  