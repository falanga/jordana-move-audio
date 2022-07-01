## Tratamento dos arquivos de audio para separação em diretórios

import os
from typing import List

from util import get_dir, get_nome_info

# Define o diretório de busca para tratamento dos arquivos (base do audio)
diretorio_base = "/home/falanga/Downloads/jordana-py/audio02-1/audio/"

diretorio_destino = "/home/falanga/Downloads/jordana-py/saida/"

nome_arquivo_de_definicao_de_nome = "/home/falanga/workspaces/conda/jordana/speaker_wordlist.cvs"

# Recupera os diretórios de control e dysarthric
lista_base_de_diretorios = get_dir(diretorio_base, 1)

# Trata cada um dos diretórios
for diretorio in lista_base_de_diretorios:
    print("Trabalhando no diretório:", diretorio)
    # Recupera os diretórios internos na pasta
    lista_interna = get_dir(diretorio_base + diretorio, 1)
    # Trata cada um dos diretórios
    for diretorio_interno in lista_interna:
        diretorio_atual = diretorio_base + diretorio + "/" + diretorio_interno
        print("Trabalhando os arquivos no diretorio: ", diretorio_atual)
        # Recupera os nomes dos arquivos presentes no diretório
        listaDeFiles: list[str] = get_dir(diretorio_atual, 0)
        # Atribui as palavras faladas no audio ao nome do arquivo de acordo com a lista em speaker_wordlist.cvs
        lista_de_arquivos_com_informacoes_de_tipo = get_nome_info(listaDeFiles, nome_arquivo_de_definicao_de_nome)
        # Move cada um dos arquivos para o destino
        for nome_do_arquivo, padrao_possivel_de_nome in lista_de_arquivos_com_informacoes_de_tipo.items():
            arquivo_origem = diretorio_atual + "/" + nome_do_arquivo
            print("\tOrigem:", arquivo_origem)
            diretorio_destino_completo = diretorio_destino + diretorio + "/" + padrao_possivel_de_nome
            arquivo_destino = diretorio_destino_completo + "/" + nome_do_arquivo
            print("\tDestino:",arquivo_destino)
            # Se o diretório de saida não existe, cria
            if not os.path.exists(diretorio_destino_completo):
                print("Cria diretorio:", diretorio_destino_completo)
                os.makedirs(diretorio_destino_completo)
            # Movimenta os arquivos da origem ao destino
            os.rename(arquivo_origem, arquivo_destino)

exit(0)



