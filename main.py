class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"hello my name is {self.name}.")

tom = Robot("jom")
jerry = Robot("jerry")

tom.introduce()
jerry.introduce()