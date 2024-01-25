steps_count = 0
has_failed = False

while steps_count < 10000:
    command = input()
    if command != "Going home":
        steps = int(command)
        steps_count += steps
    else:
        steps = int(input())
        steps_count += steps
        if steps_count < 10000:
            has_failed = True
        break

if not has_failed:
    print("Goal reached! Good job!")
    print(f"{steps_count - 10000} steps over the goal!")
else:
    print(f"{10000 - steps_count} more steps to reach goal.")
