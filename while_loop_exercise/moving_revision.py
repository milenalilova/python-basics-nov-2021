length = int(input())
width = int(input())
height = int(input())

space = length * width * height

command = input()

while space > 0:
    if command == "Done":
        print(f"{space} Cubic meters left.")
        break

    else:
        boxes = int(command)
        space -= boxes
        if space <= 0:
            print(f"No more free space! You need {abs(space)} Cubic meters more.")
            break

    command = input()
