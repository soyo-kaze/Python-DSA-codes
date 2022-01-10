import copy

class Person:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        self.note = "s"

    def Speak(self):
        print("my name is {} and I am {} yr old".format(self._name, self._age))


sam = Person('sameer', 21)
sam.Speak()
sam.note = "sam"
sami = Person("sad",23)
sami.note = sam.note
sam.note = '21'
print(sami.note,sam.note)