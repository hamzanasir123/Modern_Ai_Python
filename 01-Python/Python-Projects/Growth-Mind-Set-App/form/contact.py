import streamlit as st
import re
import requests

# WEBHOOK_URL = ""


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button: 
            if not name:
                st.error("Please Provide Your Name." , icon=":material/chat:")
                st.stop()

            if not email:
                st.error("Please Provide Your Email." , icon=":material/chat:")
                st.stop()

            if not is_valid_email(email):
                st.error("Please Provide Your Valid Email Address." , icon=":material/chat:")
                st.stop()

            if not message:
                st.error("Please Provide A Message." , icon=":material/chat:")
                st.stop()

            st.success("Form Submit Successfully!")

            # data = {"email": email, "name" : name, "message" : message}
            # response = requests.post(WEBHOOK_URL, json=data)