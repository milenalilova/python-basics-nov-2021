text = input()
vocals_sum = 0

for letter in text:
    if letter == "a":
        vocals_sum += 1

    elif letter == "e":
        vocals_sum += 2

    elif letter == "i":
        vocals_sum += 3

    elif letter == "o":
        vocals_sum += 4

    elif letter == "u":
        vocals_sum += 5

print(vocals_sum)
