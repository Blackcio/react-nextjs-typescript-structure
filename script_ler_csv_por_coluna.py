from meusmetodos import escolher_arquivo, input_tkinter, ler_colunas, perguntar_sim_nao
from csv import DictReader

#escolher um arquivo CSV para iterar
arquivo_csv = escolher_arquivo()

#ler arquivo CSV e mostrar as colunas da tabela
ler_colunas(arquivo_csv)

#abre o arquivo e lista a coluna desejada
with open(arquivo_csv, encoding='utf-8') as meuscv:
    separador = input_tkinter('informe o separador deste CSV:') # FUNÇAO DE INPUT TK
    reader = DictReader(meuscv, delimiter=separador)            # LER O ARQIVO CSV
    coluna = input_tkinter('qual coluna quer escolher?')        # FUNÇÃO DE INPUT TK
    for linha in reader:
        print(linha[coluna])
        print(linha)
        print('--------------')


#   Teste de MEUS METODOS - Perguntar SIM ou NÂO
resposta = perguntar_sim_nao('quer continuar?')
if resposta:
    print(resposta)
else:
    print(resposta)

