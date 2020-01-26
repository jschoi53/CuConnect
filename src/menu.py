import kivy
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox 

class HobbyChooser(Screen):
    hobbies = ObjectProperty(None)

    hobbylist = []

    def on_checkbox_active(self, checkboxInstance, isActive): 
        if isActive: 
            self.hobbylist.append(checkboxInstance) 
        else: 
            self.hobbylist.remove(checkboxInstance)

    def profile(self):
        if len(self.hobbylist) > 5 or len(self.hobbylist) < 1:
            return subbutt()
        else:
            # self.reset()
            sm.current = "main"
            print(self.hobbylist)


    def reset(self):
        self.major.text = ""

class FillUserInfo(Screen):
    major = ObjectProperty(None)
    course = ObjectProperty(None)

    courselist = []
    
    def on_checkbox_active(self, checkboxInstance, isActive): 
        if isActive: 
            #self.lbl_active.text ="Checkbox is ON"
            #print("Checkbox Checked" + checkboxInstance)
            self.courselist.append(checkboxInstance) 
        else: 
           # self.lbl_active.text ="Checkbox is OFF"
            #print("Checkbox unchecked "+ checkboxInstance)
            self.courselist.remove(checkboxInstance)
        print(self.courselist)

    def hobbies(self):
        if len(self.courselist) > 5 or len(self.courselist) < 1:
            return subbutt()
        else:
            # self.reset()
            sm.current = "hobbies"

    def reset(self):
        self.major.text = ""


            

    # def courseBtn(self):
    #     print("Class Press")
    
    # def hobbiesBtn(self):
    #      print("Hobbies Press")
    

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def loginBtn(self):
        print(self.username.text)
        self.reset()
        sm.current="main"

    def reset(self):
        self.username.text = ""
        self.password.text = ""

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        self.reset()
        sm.current = "login"

    def submit(self):
        self.reset()
        sm.current = "userinfo"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm:current = "login"

    def on_enter(self, *args):
        self.n.text = "Account Name: Jamie"
        self.email.text = "Email: Ketchup@gmail.com"
        self.created.text = "Created On: Now"

def subbutt():
    pop = Popup(title='Too many chosen', 
                    content=Label(text="Pick between one and\n five options, please"), size_hint=(None,None), size=(400,300))
    pop.open()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), 
            CreateAccountWindow(name="create"), 
            MainWindow(name="main"), 
            FillUserInfo(name="userinfo"),
            HobbyChooser(name="hobbies")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()