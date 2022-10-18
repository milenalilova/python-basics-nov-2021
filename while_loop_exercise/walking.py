command = input()
steps_sum = 0

while True:
    if command == "Going home":
        steps_made = int(input())
        steps_sum += steps_made
        if steps_sum < 10000:
            print(f"{10000 - steps_sum} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{steps_sum - 10000} steps over the goal!")
        break
    steps_made = int(command)
    steps_sum += steps_made
    if steps_sum >= 10000:
        print("Goal reached! Good job!")
        print(f"{steps_sum - 10000} steps over the goal!")
        break
    command = input()

#  Badly written. To optimize it.
