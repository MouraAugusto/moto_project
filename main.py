import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.popup import Popup

class TestApp(App):

    def build(self):

        self.test=FloatLayout()
        dropdown = DropDown()

        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        img1=Image(source='blue-slate.jpg', allow_stretch=True,keep_ratio=False)
        busca=TextInput(font_size=30, hint_text='->inserir local de partida', size_hint=(.45, .10), pos_hint=({"center_x":.43, "center_y":.775}))
        button=Button(text='Ir!',  pos_hint=({"center_x":.71, "center_y":.775}), size_hint=(.10, .10), font_size=30, on_release=self.incrementar)
        dropbutton=Button(text='Menu',pos_hint=({"center_x":.07, "center_y":.90}),size_hint=(.10,.10))

        dropbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(dropbutton, 'text', x))
        
        self.test.add_widget(img1)
        self.test.add_widget(busca)
        self.test.add_widget(button)
        self.test.add_widget(dropbutton)

        return self.test


    def incrementar(self,button):

        popup = Popup(title='Atencao!!!',content=Label(text='Sua moto esta a caminho'),size_hint=(None, None), size=(300, 300), pos_hint=({"center_x":.50, "center_y":.50}),auto_dismiss=True)
        popup.open()


if __name__ == '__main__':
    TestApp().run()
