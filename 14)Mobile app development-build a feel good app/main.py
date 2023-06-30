#naming a mobile app 'main.py' 
#it is good idea to name as main.py
#when you deploy or convert an app to an executable mobile app that will run on a mobile phone
# it is a good idea to name it as it or you wil run into errors
#there are two ways in making an app one in which placing everything in the py file or dividing it into design and logic file.
#normally all the professionals use the second type to create a mobile app.
#the instructor is teaching us only that method.
from kivy.app import App
from kivy.lang import Builder
#this builder enables us to access the design file.
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    pass
    
class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__=="__main__":
    MainApp().run()