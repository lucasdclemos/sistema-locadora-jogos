estoque_dict = {}
jogos_alugados_dict = {}

def adiciona_jogo_catalogo(nome):
    novo_id = len(estoque_dict) + 1
    dict_auxiliar = dict(nome = nome, quantidade = 2)
    estoque_dict.update({novo_id: dict_auxiliar})
    return

def cadastrar_jogo_alugado(nome, usuario_id):
    auxiliar = verifica_estoque(nome)
    if auxiliar == 1:
        dict_auxiliar = dict(jogo = nome)
        jogos_alugados_dict.update({usuario_id: dict_auxiliar})
        print("O jogo foi alugado com sucesso")
    elif auxiliar == 0:
        # Solicitar jogo novo pros fornecedores
        print("Não há exemplares do jogo em estoque ")
    else:
        print("O jogo não existe no estoque")

def verifica_estoque(nome):
    for jogo in estoque_dict:
        if estoque_dict[jogo]["nome"] == nome:
            if estoque_dict[jogo]['quantidade'] > 0:
                return 1
            else:
                return 0
    return -1

