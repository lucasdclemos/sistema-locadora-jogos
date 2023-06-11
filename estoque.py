estoque_dict = {}
jogos_alugados_dict = {}

def adiciona_jogo_catalogo(nome):
    novo_id = len(estoque_dict) + 1
    dict_auxiliar = dict(nome = nome, quantidade = 2)
    estoque_dict.update({novo_id: dict_auxiliar})
    return

def cadastrar_jogo_alugado(nome, usuario_id):
    dict_auxiliar = dict(nome = nome, quantidade = 2)
    estoque_dict.update({novo_id: dict_auxiliar})


adiciona_jogo_catalogo("Jogo da Vida")
adiciona_jogo_catalogo("Banco Imobiliário")
adiciona_jogo_catalogo("Uno")
print(estoque_dict)
