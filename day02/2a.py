score = 0
offset = 23
base = 87

for line in open('input.txt'):
    ascii_code = ord(line[2])
    score += ascii_code - base
    decrypted = chr(ascii_code - offset)
    if line[0] == decrypted:
        score += 3
    elif line[0] == 'C' and decrypted == 'A':
        score += 6
    elif line[0] < decrypted:
        if not (line[0] == 'A' and decrypted == 'C'):
            score += 6

print(score)
