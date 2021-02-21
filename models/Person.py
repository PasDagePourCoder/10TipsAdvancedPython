from dataclasses import dataclass
from enum import Enum


class Person:

    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


@dataclass(frozen=False)
class Person:
    name: str
    age: int
    gender: Gender


