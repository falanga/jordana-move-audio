from os import replace, walk
from gettext import find


def get_diferenca(dirOrigem, dirDestino):
    files_origem = get_dir(dirOrigem)
    files_destino = get_dir(dirDestino)
    return list(set(files_origem) - set(files_destino))


def get_lista_de_padroes_de_nomes(nomeArquivo):
    ref_arquivo = open(nomeArquivo, "r")

    lista = dict()
    for linha in ref_arquivo:
        if len(linha.strip()) > 0:
            valores = linha.split(";")
            lista.update({valores[1].strip(): valores[0]})
    ref_arquivo.close()
    return lista

def get_dir(diretorio, tipo):
    f = []
    files = []

    for (dirpath, dirnames, filenames) in walk(diretorio):
        if tipo == 0:
            f.extend(filenames)
        elif tipo == 1:
            f.extend(dirnames)
        # elseif (tipo == 3)
        #     f.extend(dirpath)
        break

    f.sort()
    return f

def get_nome_info(listNomes, arquivo_de_padrao_de_nomes):
    # Recupera os padrões de nomes do arquvivo CVS
    padroesDeNomes = get_lista_de_padroes_de_nomes(arquivo_de_padrao_de_nomes)

    lista = dict()
    for nome in listNomes:
        campos=nome.split("_")
        palavra_falada = padroesDeNomes.get(campos[1] + "_" + campos[2])
        if (palavra_falada is None):
            palavra_falada = padroesDeNomes.get(campos[2])

        lista[nome] = palavra_falada

    return lista


