import flet as ft

def main(page: ft.Page):

    page.title = "MR 3D Studio"
    page.bgcolor = ft.colors.TRANSPARENT  # Fundo transparente para ver a imagem de fundo

    # Imagem de fundo
    background_image = ft.Image(
        src="layout.png",  # Caminho para a imagem
        fit=ft.ImageFit.COVER,  # Preencher toda a área
        width=page.width,
        height=page.height,
    )

    # Dicionário para armazenar a quantidade de imagens de cada ambiente
    ambientes = {
        "Dormitório": 0,
        "Banheiro": 0,
        "Lavabo": 0,
        "Cozinha": 0
    }

    # Dicionário para armazenar a seleção de serviços por ambiente
    servicos = {
        "Dormitório": {"planta": False, "detalhamento": False, "imagens": True},
        "Banheiro": {"planta": False, "detalhamento": False, "imagens": True},
        "Lavabo": {"planta": False, "detalhamento": False, "imagens": True},
        "Cozinha": {"planta": False, "detalhamento": False, "imagens": True}
    }

    # Custos dos serviços
    custos_servicos = {
        "planta": 200,          # Exemplo: custo por planta
        "detalhamento": 150,    # Exemplo: custo por detalhamento
        "imagens": 100          # Custo por imagem
    }

    # Função para calcular o preço total com base na quantidade de imagens e serviços selecionados
    def atualizar_preco():
        total = sum(ambientes.values()) * custos_servicos["imagens"]  # Cálculo de imagens
        for ambiente, servicos_ambiente in servicos.items():
            for servico, selecionado in servicos_ambiente.items():
                if selecionado and servico != "imagens":  # Evitar duplicar o cálculo das imagens
                    total += custos_servicos[servico]
        total_label.value = f"Preço total: R$ {total:.2f}"
        page.update()

    # Função para mudar a quantidade de imagens de um ambiente e atualizar o display
    def mudar_quantidade(ambiente, incremento):
        ambientes[ambiente] += incremento
        if ambientes[ambiente] < 0:
            ambientes[ambiente] = 0
        quantidade_labels[ambiente].value = str(ambientes[ambiente])  # Atualiza o valor exibido
        atualizar_preco()

    # Função para lidar com a seleção de serviços
    def selecionar_servico(ambiente, servico, selecionado):
        servicos[ambiente][servico] = selecionado
        atualizar_preco()

    # Lista para armazenar os elementos que mostram a quantidade de imagens
    quantidade_labels = {}

    # Criação de uma lista de contadores e checkboxes para cada ambiente
    lista_ambientes = []
    for ambiente in ambientes.keys():
        quantidade_label = ft.Text(str(ambientes[ambiente]), key=ambiente, width=10, size=16, color=ft.colors.WHITE70)
        quantidade_labels[ambiente] = quantidade_label  # Armazena referência ao Text de quantidade
        # --- Ajuste o tamanho do texto do nome do ambiente ---
        l_planta = ft.Text(value='Planta', width=10, size=16, color=ft.colors.WHITE)
        print(l_planta)
        print(type(l_planta))
        l_planta = str(l_planta)
        print(type(l_planta))
        print(l_planta)

        contador = ft.Row([
            ft.Text(ambiente, width=100, size=16, color=ft.colors.WHITE70),
            ft.IconButton(ft.icons.REMOVE, on_click=lambda e, amb=ambiente: mudar_quantidade(amb, -1)),
            quantidade_label,
            ft.IconButton(ft.icons.ADD, on_click=lambda e, amb=ambiente: mudar_quantidade(amb, 1)),
            # Caixas de seleção para os serviços
            ft.Checkbox(label=l_planta, on_change=lambda e, amb=ambiente: selecionar_servico(amb, "planta", e.control.value)),
            ft.Checkbox(label="Detalhamento", on_change=lambda e, amb=ambiente: selecionar_servico(amb, "detalhamento", e.control.value)),
            ft.Checkbox(label="Imagens", on_change=lambda e, amb=ambiente: selecionar_servico(amb, "imagens", e.control.value), value=True)  # Padrão imagens já selecionado
        ])
        lista_ambientes.append(contador)

    # Label para mostrar o preço total
    total_label = ft.Text("Preço total: R$ 0.00", size=20)

    # Layout final com as colunas acima da imagem de fundo
    page.add(
        ft.Stack(
            [
                # Imagem de fundo que cobre toda a tela
                ft.Container(
                    background_image,
                    expand=True
                ),
                # Colunas sobre a imagem de fundo
                
                ft.Column(
                    lista_ambientes + [total_label],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ]
        )
    )

# Executa o aplicativo no Flet
ft.app(target=main)
