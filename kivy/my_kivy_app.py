import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='Click me')
        button.bind(on_press=self.on_button_click)
        return button

    def on_button_click(self, instance):
        print('Button clicked!')

if __name__ == '__main__':
    MyApp().run()
