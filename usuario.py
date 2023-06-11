# Inicializando estrutura que controla os usuarios
usuarios_dict = {}

# Função para adicionar o cadastro de um usuário novo 
def adiciona_usuario(id, nome_usuario):
    dict_auxiliar = dict(nome =  nome_usuario)
    usuarios_dict.update({id: dict_auxiliar})
    return
    
# Função para procurar um usuário entre todos os cadastrados
def verifica_usuario(nome):
    contador_id = 1
    for usuario in usuarios_dict.values():
        if nome == usuario["nome"]:
            print("Usuário " + nome + " encontrado")
            print("ID:", contador_id)
            return
        contador_id += 1
    adiciona_usuario(contador_id, nome)
    return

print(usuarios_dict)
verifica_usuario("Lucas Lemos")
verifica_usuario("Maristela Demarco")
verifica_usuario("Luana Franco")
verifica_usuario("Luana Franco")
print(usuarios_dict)



