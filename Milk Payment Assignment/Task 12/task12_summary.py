# Task 12: Milk Payment Calculator Summary

print("VILLAGE MILK CO-OPERATIVE")
print("-------------------------")
print("Base rate: Rs. 30.00 per litre")
print("Standard fat: 3.5%")
print("Standard SNF: 8.5%")
print("Fat adjustment: Rs. 0.40 per 0.1%")
print("SNF adjustment: Rs. 0.30 per 0.1%")

print("\nExample Payment")

litres = 10
fat = 3.5
snf = 8.5
rate = 30.00
payment = litres * rate

print("Milk quantity:", litres, "litres")
print("Fat percentage:", fat)
print("SNF percentage:", snf)
print(f"Rate per litre: Rs. {rate:.2f}")
print(f"Total payment: Rs. {payment:.2f}")