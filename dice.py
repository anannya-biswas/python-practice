import random

while True:
    roll = input("Roll the dice? (y/n): ")
    if roll.lower() == 'y':
        print("You rolled:", random.randint(1, 6))
    else:
        print("Goodbye!")
        break
