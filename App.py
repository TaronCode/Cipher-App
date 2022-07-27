from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.theming import ThemeManager
def Cipher(step, text):
    rus_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_text = ""

    for i in text:
        if i in eng_upper_alphabet or i in eng_lower_alphabet:
            if i.islower():
                ret_text += eng_lower_alphabet[(eng_lower_alphabet.index(i) + step) % 26]
            elif i.isupper():
                ret_text += eng_upper_alphabet[(eng_upper_alphabet.index(i) + step) % 26]


        elif i in rus_upper_alphabet or i in rus_lower_alphabet:
            if i.islower():
                ret_text += rus_lower_alphabet[(rus_lower_alphabet.index(i) + step) % 32]
            elif i.isupper():
                ret_text += rus_upper_alphabet[(rus_upper_alphabet.index(i) + step) % 32]
        else:
            ret_text += i

    return ret_text

def disCipher(step, text):
    rus_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_text = ""

    for i in text:
        if i in eng_upper_alphabet or i in eng_lower_alphabet:
            if i.islower():
                ret_text += eng_lower_alphabet[(eng_lower_alphabet.index(i) - step) % 26]
            elif i.isupper():
                ret_text += eng_upper_alphabet[(eng_upper_alphabet.index(i) - step) % 26]
        elif i in rus_upper_alphabet or i in rus_lower_alphabet:
            if i.islower():
                ret_text += rus_lower_alphabet[(rus_lower_alphabet.index(i) - step) % 32]
            elif i.isupper():
                ret_text += rus_upper_alphabet[(rus_upper_alphabet.index(i) - step) % 32]
        else:
            ret_text += i

    return ret_text

class Container(MDFloatLayout):
    def change_text_cipher(self):
        if self.shear_step.text != "" and self.shear_step.text.isnumeric():
            self.text_to_result.text = Cipher(int(self.shear_step.text), self.text_for_result.text)
        if self.shear_step.text == "":
            self.text_to_result.text = self.text_for_result.text

    def change_text_discipher(self):
        if self.shear_step.text != "" and self.shear_step.text.isnumeric():
            self.text_for_result.text = disCipher(int(self.shear_step.text), self.text_to_result.text)
        if self.shear_step.text == "":
            self.text_for_result.text = self.text_to_result.text

    def step_on_text(self):
        if len(self.text_to_result.text) < len(self.text_for_result.text):
            self.change_text_cipher()
        elif len(self.text_for_result.text) < len(self.text_to_result.text):
            self.change_text_discipher()
        elif len(self.text_to_result.text) == len(self.text_for_result.text):
            self.change_text_cipher()

class TextApp(MDApp):
    theme_cls = ThemeManager()
    title = "Cipher App"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Container()

if __name__ == "__main__":
    TextApp().run()