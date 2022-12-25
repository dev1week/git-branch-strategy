class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator = self.view.cb.currentText()

        if operator == '+':
            return f'{num1}+{num2}={self.sum(num1, num2)}'
        else:
            return "Calculate Error"
    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(lambda:self.view.clearMessage)
    def sum(self, a, b):
        try:
            return a+b 
        except:
            return "Calculation Error"
    def sub(self, a,b):
        return a-b
    def mul(self, a,b):
        return a*b 
    def dev(self, a,b):
        return a/b
    def pow(self, a,b):
        return pow(a,b)