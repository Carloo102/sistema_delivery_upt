from flet import Container, Column, Text

class PanelLogin(Container):
    def __init__(self) -> None:
        super() .__init__()

        self.content = Column(
            controls=[
                Text("Sistema delivery"),
                

            ]
        )