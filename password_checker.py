import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc).")

    strength_levels = {
        5: "Very Strong ",
        4: "Strong ",
        3: "Moderate ",
        2: "Weak ",
        1: "Very Weak ",
        0: "Extremely Weak ",
    }

    return strength_levels[score], feedback

password = input("Enter a password to check strength: ")
strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)
print("\nFeedback:")
if feedback:
    for f in feedback:
        print("- " + f)
else:
    print("Your password meets all requirements! ✔")