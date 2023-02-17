import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MessageToGodApp(App):
    def build(self):
        self.label = Label(text="Enter your message:")
        self.text_input = TextInput(multiline=False)
        self.button = Button(text="Send", on_press=self.send_message)
        self.output_label = Label(text="")

        self.root = BoxLayout(orientation="vertical")
        self.root.add_widget(self.label)
        self.root.add_widget(self.text_input)
        self.root.add_widget(self.button)
        self.root.add_widget(self.output_label)
        return self.root

    def send_message(self, instance):
        message = self.text_input.text
        self.output_label.text = f"Your message to God was: {message}"

if __name__ == "__main__":
    app = MessageToGodApp()
    app.run()
