# Task 10: Input Validation

def valid_entry(litres, fat, snf):
    if litres <= 0:
        return False

    if fat < 2.0 or fat > 7.0:
        return False

    if snf <= 0:
        return False

    return True


# Test different inputs
print("Valid entry:", valid_entry(10, 3.5, 8.5))
print("Invalid litres:", valid_entry(-5, 3.5, 8.5))
print("Invalid fat:", valid_entry(10, 8.0, 8.5))
print("Invalid SNF:", valid_entry(10, 3.5, -1))