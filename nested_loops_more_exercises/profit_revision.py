coin_one_lv = int(input())
coin_two_lv = int(input())
note_five_lv = int(input())
amount_lv = int(input())

for i in range(coin_one_lv + 1):
    for j in range(coin_two_lv + 1):
        for k in range(note_five_lv + 1):
            sum_lv = i * 1 + j * 2 + k * 5
            if sum_lv == amount_lv:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum_lv} lv.")
