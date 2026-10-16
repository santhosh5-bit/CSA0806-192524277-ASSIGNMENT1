# Task 3: Choose Variables and Name Constants

BASE_RATE = 30.00
FAT_RATE = 0.40
SNF_RATE = 0.30

MIN_FAT = 2.0
MAX_FAT = 7.0
BASE_FAT = 3.5
BASE_SNF = 8.5

litres = 10
fat = 4.2
snf = 8.7

fat_steps = round((fat - BASE_FAT) / 0.1)
snf_steps = round((snf - BASE_SNF) / 0.1)

rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
amount = litres * rate

print("Base rate:", BASE_RATE)
print("Fat rate:", FAT_RATE)
print("SNF rate:", SNF_RATE)
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Total payment: Rs.", round(amount, 2))

# Dynamic typing
value = 10
print("Integer value:", value)

value = "Milk"
print("String value:", value)

# Multiple assignment and swapping
a = 5
b = 10
a, b = b, a
print("After swapping:", a, b)