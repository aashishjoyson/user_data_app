import streamlit as st
import mysql.connector
from mysql.connector import Error
import re

# Database connection function
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",   # Replace with your MySQL username
        password="yourpassword",  # Replace with your MySQL password
        database="user_data"
    )

# Function to create a new user in the database
def insert_user(name, email, age, dob):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email, age, dob) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, age, dob))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        st.error(f"Error: {e}")

# Function to retrieve all users from the database
def get_users():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Error as e:
        st.error(f"Error: {e}")
        return []

# Streamlit app
st.title("User Data Input Form")

# Form input fields
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1)
    dob = st.date_input("Date of Birth")
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Basic validation
        if not name:
            st.error("Name is required.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Invalid email format.")
        elif age <= 0:
            st.error("Age must be a positive integer.")
        else:
            # Insert user into the database
            insert_user(name, email, age, dob)
            st.success("User data submitted successfully!")

# Display the data in a table format
st.subheader("User Data")
users = get_users()
if users:
    st.table(users)
else:
    st.info("No data available.")
