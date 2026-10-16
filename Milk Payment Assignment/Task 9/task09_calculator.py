# Task 9: Milk Payment Calculator

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5


def rate_per_litre(fat, snf):
    fat_steps = round((fat - BASE_FAT) / 0.1)
    snf_steps = round((snf - BASE_SNF) / 0.1)
    return round(
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE, 2
    )


def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)


def valid_entry(litres, fat, snf):
    return (
        litres > 0
        and 2.0 <= fat <= 7.0
        and snf > 0
    )


def main():
    total = 0.0

    for number in range(1, 6):
        print("\nEntry", number)

        try:
            litres = float(input("Enter litres: "))
            fat = float(input("Enter fat percentage: "))
            snf = float(input("Enter SNF percentage: "))
        except ValueError:
            print("Invalid input. Enter numbers only.")
            continue

        if not valid_entry(litres, fat, snf):
            print("Invalid entry. Check litres, fat and SNF.")
            continue

        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        total += amount

        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment: Rs. {amount:.2f}")

    print(f"\nTotal payment: Rs. {total:.2f}")


if __name__ == "__main__":
    main()