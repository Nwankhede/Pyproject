#Class for a Robot

class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.internal_temperature = 25.0

    def say_hi(self):
        print("Hello, my name is "+ self.name)
