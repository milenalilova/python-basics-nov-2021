w = int(input())
l = int(input())
h = int(input())
cubic_meters = w * l * h

while True:
    command = input()
    if command == "Done":
        print(f"{cubic_meters} Cubic meters left.")
        break
    boxes = int(command)
    cubic_meters -= boxes
    if cubic_meters <= 0:
        print(f"No more free space! You need {abs(cubic_meters)} Cubic meters more.")
        break
