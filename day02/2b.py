score = 0
base = 64

for line in open('input.txt'):
    match line[2]:
        case 'X':
            if line[0] == 'A':
                score += 3
            else:
                score += ord(line[0]) - base - 1
        case 'Y':
            score += 3 + ord(line[0]) - base
        case 'Z':
            score += 6
            if line[0] == 'C':
                score += 1
            else:
                score += ord(line[0]) - base + 1

print(score)
