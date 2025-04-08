import streamlit as st
import pandas as pd
import os

st.title("📑 View Your CT1 Marks")

# Check if marks file exists
if not os.path.exists("marks.csv"):
    st.warning("Marks have not been uploaded yet. Please check back later.")
else:
    df = pd.read_csv("marks.csv")
    df.columns = df.columns.str.strip()

    uuid_input = st.text_input("Enter your UUID")
    reg_input = st.text_input("Enter your Registration Number")

    if st.button("Get Marks"):
        result = df[(df['UUID'] == uuid_input) & (df['Reg no'] == reg_input)]

        if not result.empty:
            row = result.iloc[0]
            st.success("✅ Record Found")
            st.write(f"**Name:** {row['Name']}")
            st.write(f"**CT 1 Marks:** {row['CT 1']}")
        else:
            st.error("❌ No matching record found.")

