import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import math
 
class CalcGridLayout(GridLayout):
 
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                # jika penghitungan akar
                if calculation[0] == "√":
                    #menghitung nilai dari string selain index ke 0 (simbol akar)
                    self.display.text = str(math.sqrt(int(calculation[1:len(calculation)])))
                else:
                    self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
 
class CalculatorApp(App): 
 
    def build(self):
        return CalcGridLayout()
 
calcApp = CalculatorApp()
calcApp.run()
