import streamlit as st
import mysql.connector
from mysql.connector import Error
import re
import pandas as pd
from datetime import date

# Database connection function
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # Default root user
        password="",   # Default password is often blank
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

# Function to delete a user by ID
def delete_user(user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        st.error(f"Error: {e}")

# Function to calculate age from date of birth
def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Streamlit app
st.title("User Data Input Form")

# Form input fields
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    dob = st.date_input("Date of Birth", min_value=date(1950, 1, 1))  # Adjusted min_date to 1950
    age = calculate_age(dob)
    st.text(f"Calculated Age: {age}")
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Basic validation
        if not name:
            st.error("Name is required.")
        elif not re.match(r"^[A-Za-z\s]+$", name):
            st.error("Name must contain only letters and spaces.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Invalid email format.")
        else:
            # Insert user into the database
            insert_user(name, email, age, dob)
            st.success("User data submitted successfully!")
            st.experimental_rerun()  # Refresh the app to show updated data

# Display the data in a table format
st.subheader("User Data")
users = get_users()

if users:
    df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age", "Date of Birth"])

    # Display the data as a table
    st.write(df)

    # Add delete button for each row
    for index, row in df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 2, 1, 2, 1])
        col1.write(row["ID"])
        col2.write(row["Name"])
        col3.write(row["Email"])
        col4.write(row["Age"])
        col5.write(row["Date of Birth"])
        if col6.button("Delete", key=row["ID"]):
            delete_user(row["ID"])
            st.experimental_rerun()  # Refresh the app to show updated data

    # Option to download data as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='user_data.csv',
        mime='text/csv',
    )
else:
    st.info("No data available.")
