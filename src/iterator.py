from itertools import cycle

my_fruits = ["apple", "banana", "cherry", "strawberry", "mango"]
my_drinks = ['coca', 'fanta', 'pepsi', 'juice', 'water', 'milk', 'iced_tea']


iterator_fruits = iter(my_fruits)

print(next(iterator_fruits))
print(next(iterator_fruits))
print(next(iterator_fruits))
print(next(iterator_fruits))
print(next(iterator_fruits))

cycle_fruits = cycle(my_fruits)
cycle_drinks = cycle(my_drinks)

for j in cycle_fruits:
    print(j)

# We want to find when David is drinking iced_tea with 'cherry'

condition_not_met = True
number_days = 0
idx_fruits = 0
idx_drinks = 0

while condition_not_met:

    fruit = my_fruits[idx_fruits]
    drink = my_drinks[idx_drinks]

    if fruit == 'cherry' and drink == 'iced_tea':
        break

    number_days += 1
    idx_fruits += 1
    idx_drinks += 1

    if idx_fruits == len(my_fruits):
        idx_fruits = 0
    if idx_drinks == len(my_drinks):
        idx_drinks = 0


while condition_not_met:
    fruit = next(cycle_fruits)
    drink = next(cycle_drinks)

    if fruit == 'cherry' and drink == 'iced_tea':
        break

    number_days += 1
