import sys

class Greeter:

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return self.name
