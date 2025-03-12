import string
import random
import streamlit as st
import re

# Function to generate a password with customization options
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Start with lowercase letters
    characters = string.ascii_lowercase  
    
    # Add uppercase letters if selected
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Add numbers if selected
    if use_numbers:
        characters += string.digits
    
    # Add special characters if selected
    if use_special_chars:
        characters += "!@#$%^&*()_-+=<>?"
    
    # If no characters were selected, return an error
    if len(characters) == 0:
        return "Error: No character set selected."
    
    # Randomly pick 'length' characters from the 'characters' list to form a password
    return "".join(random.choice(characters) for i in range(length))

# Function to check the strength of a password and provide feedback
def check_password_strength(password):
    score = 0  # Score to track the strength of the password
    common_passwords = ["12345678", "abc123", "Khan123", "pakistan123", "password", "qwerty"]  # List of weak passwords

    # Check if the password is too common
    if password in common_passwords:
        return "❌ This password is too common. Choose a more unique one.", "Weak"

    feedback = []  # To store feedback for the user

    # Check if password length is at least 12 characters
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 12 characters long for better security.")

    # Check if both uppercase and lowercase letters are included
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔹 Include both uppercase and lowercase letters.")

    # Check if there is at least one number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔹 Add at least one number (0-9).")

    # Check if there is at least one special character
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("🔹 Include at least one special character (!@#$%^&*).")

    # Provide feedback based on the score
    if score == 4:
        return "✅ Excellent Password! You're good to go.", "Strong"
    elif score == 3:
        return "⚠️ Good password, but consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"

# Streamlit UI setup
st.title("🔐 Password Strength Checker & Generator")

# Input section for password to check strength
check_password = st.text_input("Enter your password", type="password")

# Button to check the password strength
if st.button("Check Password Strength"):
    if check_password:  # If the user has entered a password
        result, strength = check_password_strength(check_password)
        if strength == "Strong":
            st.success(result)
            st.balloons()  # Show confetti if the password is strong
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Improve it using these tips:")
            for tip in result.split("\n"):
                st.write(tip)  # Show each tip to improve the password
    else:
        st.warning("Please enter a password.")  # If no password is entered

# Password generator section
st.subheader("Generate a Strong Password")

# User input for password customization
password_length = st.number_input("Enter the length of password", min_value=12, max_value=20, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)
use_special_chars = st.checkbox("Include Special Characters", value=True)

# Button to generate the password
if st.button("Generate Password"):
    password = generate_password(password_length, use_uppercase, use_numbers, use_special_chars)
    st.success(f"Your generated password: {password}")

# Optional: You can add a strength progress bar
if check_password:
    score = 0
    if len(check_password) >= 12: score += 1
    if re.search(r"[A-Z]", check_password) and re.search(r"[a-z]", check_password): score += 1
    if re.search(r"\d", check_password): score += 1
    if re.search(r"[!@#$%^&*()_+]", check_password): score += 1

    # The strength bar increases based on score (each point = 25%)
    strength_bar = score * 25
    st.progress(strength_bar)



