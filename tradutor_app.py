from deep_translator import GoogleTranslator
import flet as ft

''' Para gerar o executável do app:
pip install pyinstaller
pip install pillow
flet pack nome_arquivo.py --icon nome_icone.png
'''

def main(page: ft.Page):
    #evento
    def traduz(e):
        tradutor = GoogleTranslator(source='auto', target='pt')
        traducao.value = f'{tradutor.translate(texto.value)}'
        texto.value = ''
        page.update()

    page.title = " TRADUTOR - by BRUNO LUNA"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    texto = ft.TextField(label= "Texto")
    traducao = ft.Text(size=30)
    page.add(
        ft.Row(
            [ft.Text('TRADUTOR', size=40, weight= 'bold')], alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [texto], alignment=ft.MainAxisAlignment.CENTER, wrap=True
        ),
        ft.Row(
            [ft.ElevatedButton("TRADUZIR", on_click=traduz)], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [traducao], alignment=ft.MainAxisAlignment.CENTER, wrap=True
        )

    )
    page.update()
ft.app(main)
