import streamlit as st

# Set the web page config
st.set_page_config(
    page_title="CT1 Marks Portal",
    page_icon="🎓",
    layout="centered"
)

# Main title and intro message
st.title("🎓 CT1 Marks Portal")
st.markdown("""
Welcome to the CT1 Marks Portal.

- 👉 Use the **sidebar** to:
  - 📤 Upload marks (admin only)
  - 📑 View your marks (students)
  
Please make sure your UUID and Registration Number are correct when viewing marks.
""")

