from estoque import *
from caixa import  *
from usuario import *
import json

recupera_dados_caixa()
recupera_arquivo_usuario()
recupera_jogos_alugados()
recupera_estoque()

print("Digite o nome do cliente que está relacionado com o alguel. Caso desejar sair do sistema, digite 'quit' no campo de 'Nome cliente'")

while True:
  cliente = input("Nome e sobrenome do cliente: ")
  if cliente == "quit":
    salva_dados_caixa()
    salva_dados_usuarios()
    salva_dados_estoque()
    salva_dados_jogos_alugados()
    exit()
  id_cliente = verifica_usuario(cliente)
  jogo_desejado = input("Nome do jogo solicitado: ")
  print("\n")
  retorno = cadastrar_jogo_alugado(jogo_desejado, id_cliente)
  if retorno == 1:
    print("O jogo foi alugado com sucesso. O caixa da loja agora é " + str(caixa_dict['saldo']))
  elif retorno == -1:
    print("O jogo foi comprado com sucesso")
  elif retorno == -5:
    print("O fornecedor não possui o jogo em estoque")
  else:
    print("Caixa não suficiente para comprar esse jogo")
  
  print("\n")




  