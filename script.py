import re
import requests


# Check if password is in the common password list
def is_common_password(password):
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    response = requests.get(url)
    common_passwords = response.text.split("\n")
    return password in common_passwords


# Check password strength
def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check complexity
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")

    # Check if password is common
    if is_common_password(password):
        feedback.append("This password is too common! Choose a unique one.")
        strength_score = 0  # Weak password, override score

    # Determine password strength
    if strength_score >= 5:
        return "Strong 💪", feedback
    elif strength_score >= 3:
        return "Medium ⚠️", feedback
    else:
        return "Weak ❌", feedback


# Main function to take user input
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, tips = check_password_strength(password)

    print(f"\n🔍 Password Strength: {strength}")
    if tips:
        print("🛠 Suggestions to Improve:")
        for tip in tips:
            print(f"  - {tip}")
