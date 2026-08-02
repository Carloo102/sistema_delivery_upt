from flet import Page, MainAxisAlignment, CrossAxisAlignment, Colors
from views.panel_login import PanelLogin

class Ventana:
    def __init__(self, ventana: Page):
        self._ventana = ventana
        self._ventana.bgcolor = "#F1E3D3"
        self._ventana.vertical_alignment = MainAxisAlignment.CENTER
        self._ventana.horizontal_alignment = CrossAxisAlignment.CENTER
        self._ventana.title = "UPT Delivery"
        self._ventana.add(PanelLogin())
        