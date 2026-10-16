# Task 11: Testing the Milk Payment Calculator

def rate_per_litre(fat, snf):
    base_rate = 30.00
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    return round(
        base_rate + fat_steps * 0.40 + snf_steps * 0.30, 2
    )


def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)


# Test cases
print("Standard test:", rate_per_litre(3.5, 8.5))
print("Higher rate test:", rate_per_litre(4.2, 8.7))
print("Lower rate test:", rate_per_litre(3.1, 8.3))
print("Payment test:", payout(10, 3.5, 8.5))
print("Zero litres test:", payout(0, 3.5, 8.5))