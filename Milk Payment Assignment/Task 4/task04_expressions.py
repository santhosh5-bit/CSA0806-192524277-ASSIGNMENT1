# Task 4: Write Correct Expressions

BASE_RATE = 30.00
FAT_RATE = 0.40
SNF_RATE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5

fat = 4.2
snf = 8.7
litres = 10

fat_steps = round((fat - BASE_FAT) / 0.1)
snf_steps = round((snf - BASE_SNF) / 0.1)

rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
amount = litres * rate

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Total amount: Rs.", round(amount, 2))

print("Unexpected result:", 0.1 + 0.2)
print("Comparison:", 0.1 + 0.2 == 0.3)
print("Rounded steps:", round((4.2 - 3.5) / 0.1))
print("Valid fat:", 2.0 <= fat <= 7.0)