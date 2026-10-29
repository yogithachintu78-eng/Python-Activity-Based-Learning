
print("===== PASSWORD POLICY VALIDATION ENGINE =====")

password = input("Enter a sample password: ")

errors = []

# Rule 1: Minimum length
if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

# Rule 2: Uppercase letter
has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True

if not has_upper:
    errors.append("Include at least one uppercase letter.")

# Rule 3: Lowercase letter
has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True

if not has_lower:
    errors.append("Include at least one lowercase letter.")

# Rule 4: Digit
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True

if not has_digit:
    errors.append("Include at least one digit.")

# Rule 5: Special character
has_special = False
for ch in password:
    if not ch.isalnum() and not ch.isspace():
        has_special = True

if not has_special:
    errors.append("Include at least one special character.")

# Rule 6: Three identical consecutive characters
has_repetition = False

for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        has_repetition = True

if has_repetition:
    errors.append(
        "Do not repeat the same character 3 times consecutively."
    )

# Rule 7: Prohibited substrings
lower_password = password.lower()

if "password" in lower_password or "1234" in lower_password:
    errors.append(
        "Password contains a prohibited substring."
    )

# Display results
print("\n===== VALIDATION REPORT =====")

if len(errors) == 0:
    print("Password accepted.")
    print("All policy rules are satisfied.")
else:
    print("Password rejected.")
    print("Failed rules:")

    for error in errors:
        print("-", error)

print("Validation completed.")
