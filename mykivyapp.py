import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 


class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        pass

class MyApp(App):
    def build(self):
        return Label(text = "My name is Rohit")

MyApp().run()


