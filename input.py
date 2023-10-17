from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class SimpleApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.count = 0
        self.label = Label(text=f'Button pressed {self.count} times')
        self.add_widget(self.label)

        self.button = Button(text='Press me!')
        self.button.bind(on_press=self.increment_count)
        self.add_widget(self.button)

    def increment_count(self, instance):
        self.count += 1
        self.label.text = f'Button pressed {self.count} times'


class MyApp(App):
    def build(self):
        return SimpleApp()


if __name__ == '__main__':
    MyApp().run()
