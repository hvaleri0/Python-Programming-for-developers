age = 22

# oldschool
if age >= 22:
    message = "Eligible"
else:
    message = "not Eligible"

# Ternary Operator:
# message = age >= 18 ? "Eligible": "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
