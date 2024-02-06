target_height = int(input())
current_height = target_height - 30

unsuccessful_jumps = 0
total_jumps = 0

while True:
    current_jump = int(input())
    total_jumps += 1

    if current_jump > current_height:
        unsuccessful_jumps = 0

        if current_height >= target_height:
            print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
            break
        else:
            current_height += 5

    else:
        unsuccessful_jumps += 1
        if unsuccessful_jumps == 3:
            print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
            break
