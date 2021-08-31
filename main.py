import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

#define colors:
red=[1.5,1.5,3,1]
red2=[1.8,1.8,3,4]
darkRed=[1.5,1.5,3,0.3]

specRed=[1.5,1.8,3,1]

class Calculator(App):
    def build(self):
        self.solution=None
        self.operators = ["/","*","+","-","."]
        self.LastUsedOperator=None
        self.LastUsedButton=None
        MainLayout=BoxLayout(orientation="vertical")
        self.solutionDisplay=TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        MainLayout.add_widget(self.solutionDisplay)

        ButtonDraft=[
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in ButtonDraft:
            HorizontalLayoutLine=BoxLayout()
            for label in row:
                if label in self.operators:
                    tempcolor=red2
                elif label == "." or label == "C":
                    tempcolor = specRed
                else:
                    tempcolor=red
                if not (label == "." or label == "-"):
                    button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=tempcolor, color="black")
                else:
                    button = Button(text=label, font_size='30sp', pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=tempcolor, color="black")
                button.bind(on_press=self.on_button_press)
                HorizontalLayoutLine.add_widget(button)
            MainLayout.add_widget(HorizontalLayoutLine)
        EqualsButton = Button(text= "=", font_size='50sp',pos_hint={"center_x": 0.5,"center_y":0.5}, background_color=darkRed)
        EqualsButton.bind(on_press=self.on_solution)
        MainLayout.add_widget(EqualsButton)

        return MainLayout

    def on_button_press(self,instance):
        if not instance.text=="C":
            #print("display:",self.solutionDisplay.text,"AND THE SAVED SOLUTION:",str(self.solution))
            if self.solutionDisplay.text and not ((self.solutionDisplay.text[-1] in self.operators) and instance.text in self.operators) and not self.solutionDisplay.text==self.solution and not self.solutionDisplay.text[0]=="E":
                self.solutionDisplay.text  += instance.text
                self.solution==None
            elif not self.solutionDisplay.text and not instance.text in self.operators:
                self.solutionDisplay.text += instance.text
                self.solution == None
            elif not self.solutionDisplay.text and instance.text =="-":
                self.solutionDisplay.text += instance.text
                self.solution == None
            elif self.solutionDisplay.text and self.solutionDisplay.text[0]=="E" and not instance.text in self.operators:
                self.solutionDisplay.text=""
                self.solutionDisplay.text += instance.text
                self.solution == None
            elif self.solutionDisplay.text==self.solution and not instance.text in self.operators:
                self.solutionDisplay.text=""
                self.solutionDisplay.text += instance.text
                self.solution == None
            elif self.solutionDisplay.text==self.solution and instance.text in self.operators:
                self.solutionDisplay.text += instance.text
                self.solution == None
        else:
            self.solutionDisplay.text=""
    def on_solution(self,instance):
        text = self.solutionDisplay.text
        if text:
            try:
                self.solution = str(eval(self.solutionDisplay.text))
                self.solutionDisplay.text = self.solution
            except SyntaxError:
                self.solutionDisplay.text = "ERROR"
                self.solution = self.solutionDisplay.text
            except NameError:
                self.solutionDisplay.text = ""
                self.solution = None
            except ZeroDivisionError:
                self.solutionDisplay.text = "ERROR-0"
                self.solution = None

        #self.solutionDisplay.text="Idiot! Use your own head!"



if __name__== "__main__":
    Calculator().run()
