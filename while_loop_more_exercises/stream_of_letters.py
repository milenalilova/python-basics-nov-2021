import unicodedata

symbol = input()
word = ""
final_word = ""

c = 0
o = 0
n = 0

while symbol != "End":
    if symbol == "c":
        if c == 0:
            c += 1
        else:
            word += symbol
    elif symbol == "o":
        if o == 0:
            o += 1
        else:
            word += symbol
    elif symbol == "n":
        if n == 0:
            n += 1
        else:
            word += symbol
    elif symbol.isalpha():
        word += symbol

    if c > 0 and o > 0 and n > 0:
        word += " "
        c = 0
        o = 0
        n = 0
        final_word += word
        word = ""

    symbol = input()

print(final_word)
