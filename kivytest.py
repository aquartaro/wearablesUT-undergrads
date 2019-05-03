from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class DisplayMessage(App):
    def build(self):
        return Label(text="Hello")
    
uh = DisplayMessage()

uh.run()