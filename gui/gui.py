# -*- coding: utf-8 -*-
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Menu(BoxLayout):
    loginButton = ObjectProperty(None)
    logoutButton = ObjectProperty(None)
    responseButton = ObjectProperty(None)

    def initializeMenu(self):
        self.remove_widget(self.responseButton)

    def mainMenu(self):
        self.remove_widget(self.responseButton)
        self.add_widget(self.loginButton)
        self.add_widget(self.logoutButton)

    def waitingResponse(self):
        self.add_widget(self.responseButton)
        self.remove_widget(self.loginButton)
        self.remove_widget(self.logoutButton)
        Clock.schedule_once(lambda dt: self.mainMenu(), 2)

class KasvojentunnistinApp(App):
    def build(self):
        app = Menu()
        app.initializeMenu()
        return app

if __name__ == '__main__':
    KasvojentunnistinApp().run()