# Meta classes in python
class Master(type):
    def __new__(cls, name, bases, dict):
        dict["attr"] = 23
        super().__new__(cls, name, bases, dict)
        return dict

class X(metaclass=Master):
    pass

print(X)