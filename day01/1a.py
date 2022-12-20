snacks_calories = 0
most_calories_carried = 0

for line in open('input.txt'):
    item_calories = line.strip()
    if item_calories:
        snacks_calories += int(item_calories)
    else:
        if snacks_calories > most_calories_carried:
            most_calories_carried = snacks_calories
        snacks_calories = 0

print(most_calories_carried)
