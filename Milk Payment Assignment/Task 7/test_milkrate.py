import milkrate

rate = milkrate.rate_per_litre(4.2, 8.7)
amount = milkrate.payout(8.5, 4.2, 8.7)

print("Imported rate:", rate)
print("Imported payment: Rs.", amount)