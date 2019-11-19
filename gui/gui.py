from kivy.app import App
from kivy.uix.button import Button


class KasvojentunnistinApp(App):
    def build(self):
        return Button(text="Kirjaudu sisään", pos=(100,350), size_hint = (.25, .18))

if __name__ == '__main__':
    KasvojentunnistinApp().run()