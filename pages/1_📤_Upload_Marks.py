import streamlit as st
import pandas as pd
import os

# ---- ADMIN CREDENTIALS ----
USERNAME = "admin"
PASSWORD = "anad123"

st.title("🔐 Admin Login – Upload CT1 Marks")

# --- Login form ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login_form"):
        input_username = st.text_input("Username")
        input_password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if input_username == USERNAME and input_password == PASSWORD:
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
        else:
            st.error("❌ Invalid credentials.")
else:
    st.success("✅ You are logged in as admin.")
    
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df.columns = df.columns.str.strip()

            if not all(col in df.columns for col in ["Sl.NO", "Name", "Reg no", "CT 1", "UUID"]):
                st.error("❌ Excel must have the columns: Sl.NO, Name, Reg no, CT 1, UUID")
            else:
                st.write("📄 Preview of Uploaded Marks:")
                st.dataframe(df)

                if st.button("Save Marks"):
                    df.to_csv("marks.csv", index=False)
                    st.success("✅ Marks saved successfully.")
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
