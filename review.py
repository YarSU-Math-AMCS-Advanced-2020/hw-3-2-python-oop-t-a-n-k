# Класс отзывов на продукты
from enum import Enum


class Star_mark(Enum):
    FAIL = 1
    BAD = 2
    SATISFACTORY = 3
    GOOD = 4
    EXCELLENT = 5


class Review:
    def __init__(self, name: str, surname: str, text: str, star: Star_mark):
        self.client_name = name
        self.client_surname = surname
        self.text = text
        self.star = star

    def edit(self) -> None:
        new_text = input("write edited text here: ")
        self.text = new_text

    def show(self) -> None:
        review = self.client_name + " " + self.client_surname + ":\n"
        for i in range(self.star.value):
            review += "⧫"
        for i in range(5 - self.star.value):
            review += "◊"
        review += "\n" + self.text + "\n"
        print(review)
