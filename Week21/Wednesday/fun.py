import sys
import abc

class Animal(abc.ABC):
    def respond(self):
        return f"Responds: {self.speak()}"

    @abc.abstractmethod
    def speak(self):
        """
        What sound does the animal make
        """
        raise NotImplementedError("Must code what sound animal makes")

class Lion(Animal):
    def speak(self):
        return "ROAR"
l = Lion()

def hello():
    return "nice"

# print(l.respond())

sys.setprofile(hello)

hello()
