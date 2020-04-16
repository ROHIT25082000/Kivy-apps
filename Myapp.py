import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(Mygrid,self).__init__(**kwargs)
        self.cols = 1

        self.myinner = GridLayout()
        self.myinner.cols = 2

        self.myinner.add_widget(Label(text = "First Name :"))
        self.name = TextInput(multiline = False)
        self.myinner.add_widget(self.name)

        self.myinner.add_widget(Label(text = "Last Name :"))
        self.lastname = TextInput(multiline = False)
        self.myinner.add_widget(self.lastname)

        self.myinner.add_widget(Label(text = "Email Name :"))
        self.email = TextInput(multiline = False)
        self.myinner.add_widget(self.email)

        self.add_widget(self.myinner)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        name = self.name.text
        last = self.lastname.text
        email= self.email.text 
        print("First Name :",name,"Last Name :",last,"Email :",email)
        self.name.text = ""
        self.lastname.text = ""
        self.email.text = ""



class Enter_the_followingApp(App):
    def build(self):
        return Mygrid()


ck = Enter_the_followingApp().run()
ck.run()



