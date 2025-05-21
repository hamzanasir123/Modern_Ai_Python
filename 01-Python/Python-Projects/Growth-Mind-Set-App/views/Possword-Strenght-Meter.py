import streamlit as st
import re
import random
import string


st.title("Possword Strenght Meter")

COMMON_POSSWORD = ["password","123456", "qwerty", "admin", "letmein"]

def is_common_possword(possword):
    return password.lower() in COMMON_POSSWORD

def check_password_strength(password):

    if is_common_possword(password):
         print("❌ This password is too common and weak. Please choose a stronger one.")
        
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password! Excellent job.")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    # Display feedback
    st.write("\n\n".join(feedback))

def generate_strong_possword():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"

    possword = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    for _ in range(6):
        possword.append(random.choice(lowercase + uppercase + digits + special_chars))


    random.shuffle(possword)
    st.write("".join(possword))







# Get user input
password = st.text_input("Enter your password: ", type="password")

if(password):
    check_password_strength(password)



generate = st.button("Generate Possword")


if(generate):
    generate_strong_possword()

    
