
def add_numbers(*args):
    result = 0

    for n in args:
        result += n

    print("Sum:", result)


add_numbers(5, 10, 15, 20)


def generate_pokemon(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

generate_pokemon(color='blue', level=15, element='water')
generate_pokemon(color='red')

