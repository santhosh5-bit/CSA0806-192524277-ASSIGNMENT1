# Task 5: Functions for Milk Payment

BASE_RATE = 30.00
FAT_RATE = 0.40
SNF_RATE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5

def calculate_rate(fat, snf):
    fat_steps = round((fat - BASE_FAT) / 0.1)
    snf_steps = round((snf - BASE_SNF) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
    return round(rate, 2)

def calculate_payment(litres, fat, snf):
    rate = calculate_rate(fat, snf)
    amount = litres * rate
    return rate, round(amount, 2)

litres = 10
fat = 4.2
snf = 8.7

rate, amount = calculate_payment(litres, fat, snf)

print("Milk quantity:", litres, "litres")
print("Fat percentage:", fat)
print("SNF percentage:", snf)
print("Rate per litre: Rs.", rate)
print("Total payment: Rs.", amount)