
from src.person import Person

if __name__ == '__main__':
    person = Person("Mike", "Fischer", 35, "123-45-6789")

    print(person.to_string())

    first_name = person.first_name

    person.first_name = "Yegor"

    print(person.to_string())
