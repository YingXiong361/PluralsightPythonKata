class Greeter:
    def __init__(self, prefix: str = "Hello"):
        self.prefix = prefix

    def greet(self, name: str) -> str:
        return f"{self.prefix}, {name} from project1!"
