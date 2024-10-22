import plotly.graph_objects as go
import pandas as pd

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

# Exemplo de uso
df = pd.DataFrame(dict(
    categorias=['Fisico', 'Psicologico', 'Emocional', 'Espiritual', 'Pessoal', 'Profissional'],
    janeiro=[3, 2, 1, 1, 3, 3],
    fevereiro=[2, 0, 5, 3, 4, 5],
    março=[5, 3, 4, 2, 1, 4]
))

grafico_radar(df)
