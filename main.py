# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.screen import MDScreen
# from kivy.uix.screenmanager import ScreenManager, Screen

# def login():
#     # Create a layout for the login screen
#     layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
    
#     # Username label and input
#     usrnm_label = MDLabel(text='Username', halign='center')
#     usrnm_input = MDTextField(hint_text='Enter username')
#     layout.add_widget(usrnm_label)
#     layout.add_widget(usrnm_input)
    
#     # Password label and input
#     pswd_label = MDLabel(text='Password', halign='center')
#     pswd_input = MDTextField(hint_text='Enter password', password=True)
#     layout.add_widget(pswd_label)
#     layout.add_widget(pswd_input)
    
#     # Login button
#     login_button = MDRaisedButton(text='Login', pos_hint={'center_x': 0.5})
    
#     def validate(instance):
#         # Print username and password (for demonstration purposes)
#         print(f"Username: {usrnm_input.text}, Password: {pswd_input.text}")
#         # Redirect to signup screen
#         app.screen_manager.current = 'signup'
    
#     login_button.bind(on_press=validate)
#     layout.add_widget(login_button)
    
#     return layout

# def signup():
#     # Create a layout for the signup screen
#     layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
    
#     # New user label and input
#     newuser_label = MDLabel(text='New Username', halign='center')
#     newuser_input = MDTextField(hint_text='Enter new username')
#     layout.add_widget(newuser_label)
#     layout.add_widget(newuser_input)

#     # New password label and input
#     newpswd_label = MDLabel(text='New Password', halign='center')
#     newpswd_input = MDTextField(hint_text='Enter new password', password=True)
#     layout.add_widget(newpswd_label)
#     layout.add_widget(newpswd_input)
    
#     # Signup button
#     signup_button = MDRaisedButton(text='Sign up', pos_hint={'center_x': 0.5})
    
#     def register(instance):
#         # Print new user and new password (for demonstration purposes)
#         print(f"New User: {newuser_input.text}, New Password: {newpswd_input.text}")
        
#     signup_button.bind(on_press=register)
#     layout.add_widget(signup_button)
    
#     return layout

# class LoginScreen(MDScreen):
#     def __init__(self, name):
#         super().__init__(name=name)
#         self.add_widget(login())

# class SignupScreen(MDScreen):
#     def __init__(self, name):
#         super().__init__(name=name)
#         self.add_widget(signup())

# class App1(MDApp):
#     def build(self):
#         # Create the screen manager
#         self.screen_manager = ScreenManager()
#         self.screen_manager.add_widget(LoginScreen(name='login'))
#         self.screen_manager.add_widget(SignupScreen(name='signup'))
#         return self.screen_manager

# if __name__ == '__main__':
#     # Create the app instance and run it
#     app = App1()
#     app.run()

import kivy
print(kivy.__version__)
