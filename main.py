from estoque import adiciona_jogo_catalogo, cadastrar_jogo_alugado, verifica_estoque, recupera_estoque, recupera_jogos_alugados, salva_dados_estoque, salva_dados_jogos_alugados
from caixa import  recupera_dados_caixa, salva_dados_caixa
from usuario import verifica_usuario, recupera_arquivo_usuario, salva_dados_usuarios
import json

recupera_dados_caixa()
recupera_arquivo_usuario()
recupera_jogos_alugados()
recupera_estoque()

adiciona_jogo_catalogo("Jogo da Vida")
adiciona_jogo_catalogo("Banco Imobiliario")
adiciona_jogo_catalogo("Guerra Naval")

print("Digite o nome do cliente que está relacionado com o alguel. Caso desejar sair do sistema, digite -1 no campo de 'Nome cliente'")

while True:
  cliente = input("Nome e sobrenome do cliente: ")
  if cliente == "-1":
    salva_dados_caixa()
    salva_dados_usuarios()
    salva_dados_estoque()
    salva_dados_jogos_alugados()
    exit()
  id_cliente = verifica_usuario(cliente)
  jogo_desejado = input("Nome do jogo solicitado: ")
  # print(jogo_desejado)
  cadastrar_jogo_alugado(jogo_desejado, id_cliente)
