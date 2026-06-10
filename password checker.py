import re

def check_password(password):
    checks = {
        "At least 8 characters":  len(password) >= 8,
        "Uppercase letter":        bool(re.search(r'[A-Z]', password)),
        "Lowercase letter":        bool(re.search(r'[a-z]', password)),
        "Number":                  bool(re.search(r'[0-9]', password)),
        "Special character":       bool(re.search(r'[^A-Za-z0-9]', password)),
    }

    score = sum(checks.values())
    levels = ["Very weak", "Weak", "Fair", "Strong", "Very strong"]

    print(f"\nPassword: {'*' * len(password)}")
    for rule, passed in checks.items():
        icon = "✅" if passed else "❌"
        print(f"  {icon} {rule}")
    print(f"\nStrength: {levels[score - 1] if score > 0 else 'No password'} ({score}/5)")

password = input("Enter a password: ")
check_password(password)