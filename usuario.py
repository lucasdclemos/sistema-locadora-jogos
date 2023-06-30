from arquivo import arquivo_usuario, salva_dados
import json

# Inicializando estrutura que controla os usuarios
usuarios_dict = {}

def salva_dados_usuarios():
  salva_dados("arquivos/usuario.json", usuarios_dict)
  return

def recupera_arquivo_usuario():
  usuarios_dict.update(arquivo_usuario())
  # print(usuarios_dict)
  return

def valida_id(f):
  def valida(id, nome):
    if type(id) == int and id > 0:
      return f(id, nome)
    else:
      return -1
  return valida    

# Função para adicionar o cadastro de um usuário novo
@valida_id 
def adiciona_usuario(id, nome_usuario):
  dict_auxiliar = dict(nome =  nome_usuario)
  usuarios_dict.update({id: dict_auxiliar})
  return id
    
# Função para procurar um usuário entre todos os cadastrados
def verifica_usuario(nome):
  contador_id = 1
  for usuario in usuarios_dict.values():
    if nome == usuario["nome"]:
      return contador_id
    contador_id += 1
  return adiciona_usuario(contador_id, nome)






