import flet as ft

# SignUp Form
class SignUpForm(ft.UserControl):
    def __init__(self, submit_values,btn_signin):
        super().__init__()
        #Return values user and password
        self.submit_values = submit_values
        #Route to signup Form
        self.btn_signin = btn_signin
        

    def btn_signup(self, e):
        if not self.text_user.value:  
            self.text_user.error_text="Enter your username!"
            self.text_user.update()
        if not self.text_password.value:
            self.text_password.error_text="Enter your password!"
            self.text_password.update()
        else:
            #Return values 'user' and 'password' as arguments 
            self.submit_values(self.text_user.value,self.text_password.value)
    def build(self):
        self.title_form=ft.Text(
            value="Let’s get to know you!",
            color ="#181D27",
            text_align=ft.TextAlign.START,
            font_family="bold", 
            size=18 
        )
        self.title_form2=ft.Text(
            value="Enter your details to continue",
            color ="#181D27",
            text_align=ft.TextAlign.START,
            font_family="regular", 
            size=18 
        )
        self.text_user = ft.TextField(
            label="Please enter your username",
            border_radius=10,
            bgcolor=ft.colors.with_opacity(1, '#ffffff'),
            color="#181D27"
        )
        self.text_password = ft.TextField(
            label="Please enter your password", password=True, can_reveal_password=True,
            border_radius=10,
            bgcolor=ft.colors.with_opacity(1, '#ffffff'),
            color="#181D27"
        )
        self.text_signup=ft.ElevatedButton(
            text="Sign up",
            bgcolor="#FFB347",
            color="#181D27",
            width=440,
            height=50,
            on_click= self.btn_signup,
        )
        self.text_signin=ft.Row(
            controls=[
                ft.Text(value="Already have an account?",
                        color="#181D27"),
                ft.TextButton(text="Sign in",
                              on_click=self.btn_signin)
                ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        

        return ft.Container(
            width=500,
            height=430,
            bgcolor=ft.colors.with_opacity(1, '#F1F1F1'),
            padding=30,
            border_radius=10,
            content=ft.Column(
                [
                    self.title_form,
                    self.title_form2,
                    ft.Container(height=30),
                    self.text_user,
                    self.text_password,
                    ft.Container(height=10),
                    self.text_signup,
                    self.text_signin,
                    
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        )
       
