bitcoin_amount = int(input())
yuan_amount = float(input())
commission = float(input())

bitcoin_to_lv = bitcoin_amount * 1168
yuan_to_usd = yuan_amount * 0.15
yuan_to_lv = yuan_to_usd * 1.76
currency_lv_to_euro = (bitcoin_to_lv + yuan_to_lv) / 1.95
currency_lv_to_euro -= currency_lv_to_euro * commission / 100

print(f"{currency_lv_to_euro:.2f}")
