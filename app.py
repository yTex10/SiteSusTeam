import flet as ft

def main(page: ft.Page):
    page.title = "SUS Team"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO
    plataforma = page.platform

    # == appbar

    def suporte_onclick(e):
        page.launch_url("https://youtube.com")

    def dark_mode(e):
        page.theme_mode = "dark"

        page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.AIR),
        title=ft.Text("SUS Team", selectable=True),
        leading_width=40,
        actions=[
            ft.IconButton(icon=ft.icons.DARK_MODE, on_click=dark_mode),
            ft.IconButton(icon=ft.icons.LIGHT_MODE, on_click=light_mode),
            ft.ElevatedButton("Suporte", icon=ft.icons.HELP, on_click=suporte_onclick)
        ],
        bgcolor=ft.colors.BLACK12
    )
        page.update()

    def light_mode(e):
        page.theme_mode = "light"

        page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.AIR),
        title=ft.Text("SUS Team", selectable=True),
        leading_width=40,
        actions=[
            ft.IconButton(icon=ft.icons.DARK_MODE, on_click=dark_mode),
            ft.IconButton(icon=ft.icons.LIGHT_MODE, on_click=light_mode),
            ft.ElevatedButton("Suporte", icon=ft.icons.HELP, on_click=suporte_onclick)
        ],
        bgcolor=ft.colors.GREY_200
    )
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.AIR),
        title=ft.Text("SUS Team", selectable=True),
        leading_width=40,
        actions=[
            ft.IconButton(icon=ft.icons.DARK_MODE, on_click=dark_mode),
            ft.IconButton(icon=ft.icons.LIGHT_MODE, on_click=light_mode),
            ft.ElevatedButton("Suporte", icon=ft.icons.HELP, on_click=suporte_onclick)
        ],
        bgcolor=ft.colors.GREY_200
    )

    textoIntroducao = ft.Text("SUS Team é um grupo de criação de bots do discord(E outros serviços no futuro)\nSomos responsaveis pelos bots The sus bot e King Capybara[EM BREVE]", selectable=True)
    page.add(textoIntroducao)

    tituloProjetos = ft.Text("Projetos", size=30, selectable=True)
    page.add(tituloProjetos)

    infoKingCapybara = ft.Container(content=ft.Column(
        controls=[
            ft.Row(controls=[ft.Icon(ft.icons.ANIMATION_OUTLINED), ft.Text("King Capybara", size=20, weight=ft.FontWeight.BOLD, selectable=True)]),
            ft.Text("King Capybara é um bot social escrito em python e está sob nossa posse.\nO Bot tem sistemas monetarios extremamente uteis e\npersonalizaveis", selectable=True)
        ]
    ))

    infoTheSusBot = ft.Container(content=ft.Column(
        controls=[
            ft.Row(controls=[ft.Icon(ft.icons.ANIMATION_OUTLINED), ft.Text("The sus bot", size=20, weight=ft.FontWeight.BOLD, selectable=True)]),
            ft.Text("The sus bot é um bot geral escrito em python e está sob nossa posse.\nO bot fornece integração e sistemas personalizados\ndo jeito que você quiser", selectable=True)
        ]
    ))

    if plataforma in ["ios", "android"]:
        page.add(ft.Column([infoKingCapybara, infoTheSusBot]))
    else:
        page.add(ft.Row([infoKingCapybara, infoTheSusBot]))

    # == Participantes

    tituloParticipantes = ft.Text("Participantes", size=30, selectable=True)
    page.add(tituloParticipantes)

    participantesTable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Participante", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Função", weight=ft.FontWeight.BOLD))
        ],
        rows=[
            ft.DataRow([ft.DataCell(ft.Text("yTex_10")), ft.DataCell(ft.Text("Dono & Scripter"))]),
            ft.DataRow([ft.DataCell(ft.Text("Gael")), ft.DataCell(ft.Text("Administrador Geral"))]),
            ft.DataRow([ft.DataCell(ft.Text("Last")), ft.DataCell(ft.Text("Sub-Dono"))]),
            ft.DataRow([ft.DataCell(ft.Text("FBI Swat")), ft.DataCell(ft.Text("Scripter & Gerente da comunidade"))])
        ]
    )

    page.add(participantesTable)

ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER, host='0.0.0.0', port=80)
