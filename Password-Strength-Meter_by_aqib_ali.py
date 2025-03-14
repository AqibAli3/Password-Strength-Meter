import re
import random
import streamlit as st

# Password validation functions
def length_check(password):
    return len(password) >= 8

def case_check(password):
    return re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)

def digit_check(password):
    return re.search(r"\d", password)

def special_char_check(password):
    return re.search(r"[!@#$%^&*]", password)

def calculate_score(password):
    score = 0
    if length_check(password):
        score += 1
    if case_check(password):
        score += 1
    if digit_check(password):
        score += 1
    if special_char_check(password):
        score += 1
    return score

def suggest_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    feedback = []
    score = calculate_score(password)
    
    # Feedback Messages
    if not length_check(password):
        feedback.append("❌ Password should be at least 8 characters long.")
    if not case_check(password):
        feedback.append("❌ Include both uppercase and lowercase letters.")
    if not digit_check(password):
        feedback.append("❌ Add at least one number (0-9).")
    if not special_char_check(password):
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Streamlit app
def main():
    # Add custom CSS
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
            color: #333333;
        }
        h1, h2, h3 {
            color: #0B5394;
        }
        .contact-details {
            margin-top: 20px;
            text-align: center; /* Center aligns the contact section */
        }
        .contact-details img {
            width: 30px;
            margin: 10px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.title("🔑 Password Strength Meter")
    st.write("🔍 **Enter your password to check its strength and get suggestions for improvement.**")

    password = st.text_input("🔐 Enter your password:", type="password")

    if st.button("🧪 Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)

            # Display Strength Rating
            if score == 4:
                st.success("✅ **Strong Password!** Great job!")
            elif score == 3:
                st.warning("⚠️ **Moderate Password** - Consider adding more security features.")
            else:
                st.error("❌ **Weak Password** - Improve it using the suggestions below.")

            # Display Feedback
            if feedback:
                st.write("### 🔧 **Suggestions:**")
                for item in feedback:
                    st.write(item)

            # Suggest Strong Password
            if score < 4:
                suggested_password = suggest_password()
                st.write(f"🔑 **Suggested Strong Password:** `{suggested_password}`")
        else:
            st.warning("⚠️ Please enter a password to check.")

    # Collect user feedback
    st.write("---")
    st.write("### 🌟 Share Your Feedback")
    user_feedback = st.text_area("What do you think about this app? Any suggestions for improvement?", "")
    
    if st.button("📤 Submit Feedback"):
        if user_feedback:
            st.success("✅ Thank you for your feedback!")
            # Optionally, save feedback to a file or database
            with open("user_feedback.txt", "a") as file:
                file.write(user_feedback + "\n")
        else:
            st.warning("⚠️ Please enter your feedback before submitting.")

    # Contact Details Section
    st.write("---")
    st.markdown(
        """
        <div class="contact-details">
            <p>Feel free to reach out!</p>
            <a href="https://www.linkedin.com/in/syed-aqib-ali/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
            </a>
            <a href="https://github.com/AqibAli3" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub">
            </a>
            <a href="https://wa.me/+923158796106" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
            </a>
            <a href="mailto:shaali254@gmail.com">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Mail_%28iOS%29.svg" alt="Email">
            </a>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
