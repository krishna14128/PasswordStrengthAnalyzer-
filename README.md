# Password Strength Analyzer

## Project Description

The **Password Strength Analyzer** is a beginner-friendly desktop application built using **Python** and **Tkinter**.

It analyzes a user's password based on simple security rules and provides a strength score, strength level, and suggestions to improve the password.

This project is designed for beginners who want to learn Python GUI programming, regular expressions, and basic cybersecurity concepts.

---

## Features

- Check password strength
- Calculate a score from 0 to 100
- Display password strength level
  - Very Weak
  - Weak
  - Medium
  - Strong
  - Very Strong
- Show password using a checkbox
- Display helpful suggestions for improving weak passwords
- Color-changing progress bar
- Reset button
- Exit button
- Handles empty password input gracefully

---

## Technologies Used

- Python 3
- Tkinter (GUI)
- Regular Expressions (`re`)

---

## Folder Structure

PasswordStrengthAnalyzer/

├── main.py

├── analyzer.py

└── README.md

---

## How to Run the Project

### Step 1

Install Python 3 from:

https://www.python.org/

---

### Step 2

Download or clone this project.

---

### Step 3

Open a terminal or command prompt.

Navigate to the project folder.

Example:

```bash
cd PasswordStrengthAnalyzer
```

---

### Step 4

Run the application.

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## How It Works

The application checks whether the password contains:

- At least 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Each rule contributes to the overall strength score.

The application then displays:

- Password Score
- Password Strength Level
- Suggestions for improvement

---

## Screenshots

### Main Window

*(Add screenshot here)*

---

### Password Analysis

*(Add screenshot here)*

---

## Future Improvements

Possible enhancements include:

- Password entropy calculation
- Password generator
- Dark mode
- Save password history using SQLite
- Detect common passwords from a database
- Export password analysis report
- Copy generated password to clipboard
- Real-time password analysis while typing

---

## Learning Outcomes

By completing this project, you will learn:

- Python functions
- Modular programming
- Tkinter GUI development
- Regular Expressions (`re`)
- Basic password security principles
- Event-driven programming
- Input validation

---

## Author

Created as a beginner-friendly Cyber Security project using Python.