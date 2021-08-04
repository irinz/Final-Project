from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore

class DictTest(App):
    def build(self):
        # pls try the given tag dictionary here, can't do it cuz my jupyter
        # won't work for some reason
        store = JsonStore('samplewords.json')
        # Made the dictionary word1:word2 and only the 1st word is considered
        # for this

        # basically an "if word is in json" statement
        if store.exists('na'):
            self.window = GridLayout()
            self.window.cols = 1

            # label widget
            self.options = Label(text="Word exists")
            self.window.add_widget(self.options)

        else:
            self.window = GridLayout()
            self.window.cols = 1

            # label widget
            self.options12 = Label(text="Word does not exist")
            self.window.add_widget(self.options12)

        return self.window

if __name__ == "__main__":
    DictTest().run()
