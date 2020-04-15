# naming of Kivy files must me the first part of the class name (no App) in lower case, then .kv so MyApp = my.kv
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()
