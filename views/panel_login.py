from flet import Container, Column, Text, TextField, FilledButton, Control, CrossAxisAlignment, FontWeight

class PanelLogin(Container):
    def __init__(self) -> None:
        super() .__init__()
        self.inicializar_controles()

        self.content = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls= self.arreglo_controles(),
        )

    def inicializar_controles(self) -> None:
        self.lbl_iniciar_sesion = Text("Inicia sesion",
                                       weight=FontWeight.BOLD)
        self.txt_ingresar_usuario = TextField(label="Usuario")
        self.txt_ingrsar_contrasena = TextField(label="Contraseña")
        self.btn_iniciar_sesion = FilledButton("Iniciar sesion")
        self.lbl_mensaje_registrarse = Text("¿No tienes cuenta aun? Registrate")
        self.btn_registrarse = FilledButton("Registrarse")

    def arreglo_controles(self) -> list[Control]:
        return[
            self.lbl_iniciar_sesion,
            self.txt_ingresar_usuario,
            self.txt_ingrsar_contrasena,
            self.btn_iniciar_sesion,
            self.lbl_mensaje_registrarse,
            self.btn_registrarse
        ]
    
    def click_iniciar_sesion(self) -> None:
        if self.txt_ingresar_usuario.value == "Carlos" and self.txt_ingrsar_contrasena.value == "12345":
            pass
