from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

#
#    métodos usados para trazer arquivos do sistema para o código.
#
def escolher_arquivo():
    #selecionar um arquivo do computador
    arquivo = filedialog.askopenfilename()
    return arquivo

def input_tkinter(pergunta):
    digitou = simpledialog.askstring('Entrada do usuário.(string)', pergunta)
    return digitou

def perguntar_sim_nao(pergunta):
    resposta = messagebox.askyesno('Escolha do usuário', pergunta)
    return resposta


#
#   metodos usados em arquivos CSV
#
def ler_colunas(arquivo_csv):                # Mostra a primeira linha do arqivo CSV no terminal
    with open(arquivo_csv) as meuscv:
        print(meuscv.readline())

def ler_arquivo(arquivo):                          # ainda preciso melhorar esse metodo
    with open(arquivo) as arquivo_aberto:
        return arquivo_aberto


#
#   metodos que usam o PANDAS
#
def criar_df(csv):
    ler_colunas(csv)
    sep = input_tkinter('Informe o caracter separador?')
    df =pd.read_csv(csv, delimiter=sep)
    return df

def df_resumo(df):
    print(df.head())
    print('-'*20)
    print(df.axes)
    print('-'*20)
    print(df.columns)
    print('-'*20)
    print(df.values)
    print('-'*20)
    print(df.index)


def grafico_radar(df):
    fig = go.Figure()

    # Iterar sobre as colunas (excluindo a primeira que contém as categorias)
    for n_col in df.columns[1:]:
        mes = df[n_col].values
        categoria = df['categorias']

        fig.add_trace(go.Scatterpolar(
            r=mes,                            # valores dos meses
            theta=categoria,                  # categorias como ângulos
            fill='toself',
            name=n_col,                       # nome da coluna como rótulo
        ))
    
    # Configurar dinamicamente os limites do eixo radial com base nos valores do DataFrame
    max_val = df.iloc[:, 1:].max().max() + 1  # Encontrar o valor máximo e adicionar uma margem
    min_val = df.iloc[:, 1:].min().min() - 1  # Encontrar o valor mínimo e adicionar uma margem
    
    # Atualizar o layout dinamicamente
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[min_val, max_val],  # Definir o intervalo com base nos dados
                showticklabels=True        # Exibir os valores dos eixos
            )
        ),
        showlegend=True
    )
    
    return fig.show()


def salvar_df_csv(df, nome_arquivo):
    """Salve seu DataFrame em um arquivo .CSV

    Parametros:
    argumento1 = (DataFrame): deve ser um objeto DataFrame do pandas 
    argumento2 = (string)   : informe como quer salvar no HD. 'exemplo.csv'

    Returns:
    mensagem de confirmação

   """
    nome_arquivo = nome_arquivo.split('.csv')[0] + '.csv'    # revisa extenção csv

    df.to_csv(nome_arquivo, index=False)                     # salva arquivo csv no HD

    return print('Arquivo Salvo com sucesso!')               # mensagem de confirmação
