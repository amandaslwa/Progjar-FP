    ft.Column(
                    [
                        ft.Text(value="Chat List", size=30, color=ft.colors.WHITE),
                        ft.Container(
                            content=chatlist_ui,
                            width=600,
                            height=400,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            padding=20,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    height=600,
                )