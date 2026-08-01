from flet import Container, Column, Text, TextField, FilledButton, Control, CrossAxisAlignment, FontWeight, Colors

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
                                       weight=FontWeight.BOLD,)
        self.txt_ingresar_usuario = TextField(label="Usuario")
        self.txt_ingrsar_contrasena = TextField(label="Contraseña",
                                                password=True,
                                                can_reveal_password=True)
        self.btn_iniciar_sesion = FilledButton("Iniciar sesion",
                                               bgcolor=Colors.RED,
                                               on_click=self.click_iniciar_sesion)
        self.mensaje_de_texto = Text(value="")
        self.lbl_mensaje_registrarse = Text("¿No tienes cuenta aun? Registrate")
        self.btn_registrarse = FilledButton("Registrarse",
                                            bgcolor=Colors.RED)

    def arreglo_controles(self) -> list[Control]:
        return[
            self.lbl_iniciar_sesion,
            self.txt_ingresar_usuario,
            self.txt_ingrsar_contrasena,
            self.mensaje_de_texto,
            self.btn_iniciar_sesion,
            self.lbl_mensaje_registrarse,
            self.btn_registrarse
        ]
    
    def click_iniciar_sesion(self) -> None:
        self.usuario = self.txt_ingresar_usuario.value.strip()
        self.contrasena = self.txt_ingrsar_contrasena.value.strip()

        if not self.usuario or not self.contrasena:
            self.mensaje_de_texto.value = "Por favor completa todos los campos."
            self.update()
            return

        if self.usuario == "Carlos" and self.contrasena == "1234":
            self.mensaje_de_texto.value = "Bienvenido"
            self.update()
            return
            
