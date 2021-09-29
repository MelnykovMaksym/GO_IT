class People:
    def __init__(self):
        print("Can walk")
    def display (self):
        print("Hey")

class Student(People):
    def __init__(self):
        print("Want to learn fast")
        People.display(self)
        # super().display()

class PyStudent(People):
    def __init__(self):
        print("Wooohaa !")
        # People.__init__(self)
        super().__init__()

class WantRest(PyStudent, Student):
    def __init__(self):
        print("Camon")
        super().__init__()
        # Student.__init__(self)
        # PyStudent.__init__(self)

who = WantRest()
