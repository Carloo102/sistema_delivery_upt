from flet import Page

class Ventana:
    def __init__(self, ventana: Page):
        self._ventana = ventana
        self._ventana.title = "UPT Delivery"