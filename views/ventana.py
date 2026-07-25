from flet import Page
from views.panel_login import PanelLogin

class Ventana:
    def __init__(self, ventana: Page):
        self._ventana = ventana
        self._ventana.title = "UPT Delivery"
        self._ventana.add(PanelLogin())
        