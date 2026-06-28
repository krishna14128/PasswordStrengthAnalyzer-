"""
analyzer.py

This file contains all the functions required to
analyze a password and generate suggestions.
"""

import re


def calculate_password_strength(password):
    """
    Analyze the password and return:
    - score (0-100)
    - strength level
    - suggestions
    """

    score = 0
    suggestions = []

    # -----------------------------
    # Check Password Length
    # -----------------------------
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append(
            "Increase password length to at least 8 characters."
        )

    # -----------------------------
    # Check Uppercase Letters
    # -----------------------------
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters.")

    # -----------------------------
    # Check Lowercase Letters
    # -----------------------------
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters.")

    # -----------------------------
    # Check Numbers
    # -----------------------------
    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers.")

    # -----------------------------
    # Check Special Characters
    # -----------------------------
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add special characters.")

    # -----------------------------
    # Check Common Weak Patterns
    # -----------------------------
    weak_patterns = [
        "123",
        "password",
        "admin",
        "qwerty",
        "abc",
        "111",
        "000"
    ]

    password_lower = password.lower()

    for pattern in weak_patterns:
        if pattern in password_lower:
            suggestions.append("Avoid using simple patterns.")
            break

    # -----------------------------
    # Decide Strength Level
    # -----------------------------
    if score <= 20:
        level = "Very Weak"

    elif score <= 40:
        level = "Weak"

    elif score <= 60:
        level = "Medium"

    elif score <= 80:
        level = "Strong"

    else:
        level = "Very Strong"

    # -----------------------------
    # If password is strong
    # -----------------------------
    if score == 100 and len(suggestions) == 0:
        suggestions.append("Excellent! Your password is strong.")

    return score, level, suggestions