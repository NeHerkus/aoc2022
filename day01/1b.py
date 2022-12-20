snacks_calories = 0
calories_carried = []

for line in open('input.txt'):
    item_calories = line.strip()
    if item_calories:
        snacks_calories += int(item_calories)
    else:
        calories_carried.append(snacks_calories)
        snacks_calories = 0

print(sum(sorted(calories_carried)[-3:]))
