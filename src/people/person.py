class Person:
    """A class to represent a person.

    Attributes:
        name str:
            first name of the person
        surname str:
            family name of the person
        age int:
            age of the person

    Methods:
        info(additional=""):
            Prints the person's name and age.
    """

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Constructs all the necessary attributes for the person object.

        A person object.

        Args:
            name: first name of the person
            surname: family name of the person
            age: age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional: str = ""):
        """Prints the person's name and age.

        If the argument additional is passed, then it is appended after the main info.

        Args:
            additional: More info to be displayed (optional, default is None)
        """

        print(
            f"My name is {self.name} {self.surname}. I am {self.age} years old."
            + additional
        )
