from pyrsistent import b


class Calculator:

    def __init__(self, a=0, b=20) -> None:
        self.a = a
        self.b = b

    def addition(self) -> int:
        return self.a+self.b

    def substraction(self) -> float:
        return self.a-self.b        
   