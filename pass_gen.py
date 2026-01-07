import streamlit as st
import random

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_+=")

st.title("🔐 Password Generator App")

st.write("Generate strong and secure passwords easily 💪")

col1, col2, col3 = st.columns(3)

with col1:
    l = st.number_input("Letters", min_value=1, max_value=20, value=5)

with col2:
    n = st.number_input("Numbers", min_value=1, max_value=20, value=3)

with col3:
    s = st.number_input("Symbols", min_value=1, max_value=20, value=2)

if st.button("Generate Password 🚀"):
    pwd = []
    for _ in range(l):
        pwd.append(random.choice(letters))
    for _ in range(n):
        pwd.append(random.choice(numbers))
    for _ in range(s):
        pwd.append(random.choice(symbols))

    random.shuffle(pwd)
    password = "".join(pwd)

    st.success("Your Generated Password:")
    st.code(password)
    st.balloons()
