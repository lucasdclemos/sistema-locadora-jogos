import json
import os
from time import sleep
def monta_arquivo_solicitacao(nome):
  dados = json.dumps(nome, indent=4)
  arquivo_solicitacao = open("requisicao.json", "wt")
  arquivo_solicitacao.write(dados)
  arquivo_solicitacao.close()
  return

def resposta_fornecedor(nome):
  while os.path.exists("retorno.json") == False:
    sleep(0.01)
  f = open("retorno.json", "r")
  dados = f.read()
  dict = json.loads(dados)
  for jogo in dict:
    if jogo == nome:
      valor = dict[jogo]
  os.remove("retorno.json")
  return valor

def arquivo_caixa():
  f = open("arquivos/caixa.json", "r")
  dados = f.read()
  dict = json.loads(dados)
  return dict

def arquivo_usuario():
  f = open("arquivos/usuario.json", "r")
  dados = f.read()
  dict = json.loads(dados)
  return dict

def arquivo_estoque():
  f = open("arquivos/estoque.json", "r")
  dados = f.read()
  dict = json.loads(dados)
  return dict

def arquivo_jogos_alugados():
  f = open("arquivos/jogos_alugados.json", "r")
  dados = f.read()
  dict = json.loads(dados)
  return dict

def salva_dados(nome_arquivo, dict):
  f = open(nome_arquivo, "w")
  dados = json.dumps(dict)
  f.write(dados)
  f.close()
  return
