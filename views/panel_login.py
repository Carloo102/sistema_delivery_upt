from flet import Container, Column, Text, TextField, Colors, MainAxisAlignment, Alignment

class PanelLogin(Container):
    def __init__(self) -> None:
        super() .__init__()
        self.bgcolor = Colors.RED_400
        self.alignment = Alignment.CENTER

        self.content = Column(
            controls=[
                Text("Inicia sesion"),
                TextField("Usuario"),
                TextField("Contraseña"),
            ]
        )