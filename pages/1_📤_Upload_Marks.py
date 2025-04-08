import streamlit as st
import pandas as pd
import os

# ---- ADMIN CREDENTIALS ----
USERNAME = "admin"
PASSWORD = "anad123"

st.title("🔐 Admin Login – Upload CT1 Marks")

# --- Login form ---
with st.form("login_form"):
    input_username = st.text_input("Username")
    input_password = st.text_input("Password", type="password")
    login_btn = st.form_submit_button("Login")

if login_btn:
    if input_username == USERNAME and input_password == PASSWORD:
        st.success("✅ Login successful! You can now upload marks.")

        uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])
        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)
                df.columns = df.columns.str.strip()

                # Show preview
                st.write("Preview of Uploaded Marks:")
                st.dataframe(df)

                if st.button("Save Marks"):
                    df.to_csv("marks.csv", index=False)
                    st.success("✅ Marks saved successfully.")
            except Exception as e:
                st.error(f"❌ Error reading file: {e}")
    else:
        if input_username or input_password:
            st.error("❌ Invalid credentials.")
