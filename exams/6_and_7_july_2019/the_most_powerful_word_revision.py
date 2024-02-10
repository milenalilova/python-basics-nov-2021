from math import floor

word = input()
value = 0
strongest_word = ''

while word != "End of words":
    current_value = 0
    for ch in range(len(word)):
        current_value += ord(word[ch])
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' \
            or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' \
            or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' \
            or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        current_value *= len(word)
    else:
        current_value /= floor(len(word))

    if current_value > value:
        value = current_value

        strongest_word = word

    word = input()

print(f"The most powerful word is {strongest_word} - {value}")
