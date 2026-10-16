# Task 6: Organise the Logic into Functions

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5


def rate_per_litre(fat, snf):
    """Calculate and return the rate per litre."""
    fat_steps = round((fat - BASE_FAT) / 0.1)
    snf_steps = round((snf - BASE_SNF) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate and return the farmer's payment."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


def ten_day_total(payments):
    """Calculate the total payment for ten days."""
    total = 0.0
    for amount in payments:
        total += amount
    return round(total, 2)


if __name__ == "__main__":
    payments = []

    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        payments.append(amount)

        print(f"{litres:5} L  Fat {fat}  SNF {snf}  Rate {rate:6.2f}  Pay {amount:8.2f}")

    print("Ten-day total: Rs.", ten_day_total(payments))