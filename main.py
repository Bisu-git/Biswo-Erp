from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.lang import Builder

class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def login(self):
        print(f"Login attempt with email: {self.email.text}")
        print(f"Password: {self.password.text}")
    
    def go_to_register(self):
        self.manager.current = 'register'

class RegisterScreen(Screen):
    name_input = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def register(self):
        print(f"Registration attempt with:")
        print(f"Name: {self.name_input.text}")
        print(f"Email: {self.email.text}")
        print(f"Password: {self.password.text}")
    
    def go_to_login(self):
        self.manager.current = 'login'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm

if __name__ == '__main__':
    MyApp().run()