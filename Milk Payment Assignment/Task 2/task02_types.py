from decimal import Decimal

print("Type of 10:", type(10))
print("Type of 10.0:", type(10.0))
print('Type of "10":', type("10"))
print("Type of True:", type(True))
print("Type of [10, 8.5]:", type([10, 8.5]))

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

print("Decimal result:", Decimal("0.1") + Decimal("0.2"))

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

print("Decimal payment total:", total_decimal(payments))