# naming of Kivy files must me the first part of the class name (no App) in lower case, then .kv so MyApp = my.kv
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(
            "First Name: ",
            self.firstname.text,
            ", Last Name: ",
            self.lastname.text,
            ", Email: ",
            self.email.text,
        )

        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
