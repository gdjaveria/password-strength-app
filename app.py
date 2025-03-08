import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title('🔐 Password Strength Meter')

def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
        feedback.append('✅ Good Length (8+ characters)')
    else:
        feedback.append('❌ Password too short')

    # Character variety checks

    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
        
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
        
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
        
    if re.search(r"[!@#$%^&*+]", password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")

    # Simple pattern check (common passwords)
    if any(pattern in password.lower() for pattern in ['123456', 'password', 'qwerty', 'admin']):
        score = max(0, score - 1)
        feedback.append('⚠️ Contains a common password pattern')

    return score, feedback

# Password input
password = st.text_input('Enter your password', type='password')

# Show password toggle
show_password = st.checkbox('Show Password')
if show_password and password:
    st.code(password)

if password:
    score, feedback = password_strength(password)

    # Strength meter
    st.markdown("---")
    percentage = (score / 5) * 100
    st.progress(percentage / 100)

    if score >= 4:
        st.success('✅ Strong password! 😃')
    elif score >= 3:
        st.warning('⚠️ Moderate password 👍')
    else:
        st.error('❌ Weak password 🙁')

    # Show feedback
    st.markdown('### Password Check Results:')
    for item in feedback:
        st.markdown(item)





