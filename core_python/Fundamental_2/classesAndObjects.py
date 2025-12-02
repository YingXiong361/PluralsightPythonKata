 
class Robot:
    """Simple Robot class demonstrating property, classmethod, and staticmethod."""

    # class-level sequence number shared across all instances
    sequence_number = 0

    def __init__(self, name):
        self.name = name
        self.position = [0, 0]  # x, y coordinates
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] += x
        print(f'{self.name} walked to position {self.position}')

    # property getter
    @property
    def name(self) -> str:
        return self._name
    
    # property setter with simple validation
    @name.setter
    def name(self, value: str) -> None:
        if not self.is_valid_name(value):
            raise ValueError("name must be a non-empty string")
        self._name = value

    # static method for name validation (does not require class or instance)
    @staticmethod
    def is_valid_name(value: str) -> bool:
        return isinstance(value, str) and value.strip() != ""
    
    # class method to increase and return the sequence number
    @classmethod
    def increment_sequence(cls) -> int:
        cls.sequence_number += 1
        return cls.sequence_number
    
    def eat(self):
        print("I'm hungry!")

class Robot_Dog(Robot):
    """ Robot Dog subclass extending Robot functionality. """
 
    def __init__(self, name_val: str, breed_val: str):
        # call parent __init__ to reuse name validation, position setup and any prints,
        # then perform Robot_Dog-specific initialization
        # here if in the subclass we don't implement the __init__, the parent class's __init__ will be called automatically
        super().__init__(name_val)
        self.breed = breed_val

    def make_noise(self):
        print("Woof! Woof!")

    # Method overriding to change behavior from inherited eat method
    def eat(self):
        # super() allows us to call the parent class's method
        super().eat()  # call parent eat method
        print("I like bacon!")


    

if __name__ == "__main__":
    # sample usage
    dog = Robot_Dog("Buddy", "Golden Retriever")

    dog.name = "Max"
    print(dog.name)

    # demonstrate class sequence
    print("Sequence:", Robot_Dog.increment_sequence())
    print("Sequence:", Robot_Dog.increment_sequence())