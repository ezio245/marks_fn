import streamlit as st
import pandas as pd
import os

# ---- ADMIN CREDENTIALS ----
USERNAME = "admin"
PASSWORD = "anad123"

st.title("🔐 Admin Login – Upload CT1 Marks")

# --- Session-based Login ---
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

    # Reset Button
    if st.button("🧹 Reset All Marks"):
        if os.path.exists("marks.csv"):
            os.remove("marks.csv")
            st.warning("⚠️ All marks have been reset (file deleted).")
        else:
            st.info("ℹ️ No marks to reset.")

    # Upload Excel
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])
    if uploaded_file is not None:
        try:
            df_new = pd.read_excel(uploaded_file)
            df_new.columns = df_new.columns.str.strip()

            required_cols = ["Sl.NO", "Name", "Reg no", "CT 1", "UUID"]
            if not all(col in df_new.columns for col in required_cols):
                st.error("❌ Excel must have columns: Sl.NO, Name, Reg no, CT 1, UUID")
            else:
                st.write("📄 Preview of Uploaded Marks:")
                st.dataframe(df_new)

                if st.button("📥 Append to Existing Marks"):
                    if os.path.exists("marks.csv"):
                        df_existing = pd.read_csv("marks.csv")
                        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                    else:
                        df_combined = df_new

                    df_combined.to_csv("marks.csv", index=False)
                    st.success("✅ Marks appended and saved successfully.")

        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
