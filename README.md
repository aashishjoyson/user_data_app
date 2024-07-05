# User Data Input Form

This is a Streamlit application designed to manage user data within a MySQL database. Users can input their details, view all entries, delete specific entries, and download the data as a CSV file.

## Features

- **User Data Input:** Allows users to input their name, email, and date of birth.
- **Data Validation:** Ensures that the name contains only letters and spaces and the email is in a valid format.
- **Age Calculation:** Automatically calculates the user's age based on their date of birth.
- **Data Display:** Displays the entered user data in a tabular format.
- **Delete Functionality:** Allows users to delete specific entries from the database.
- **CSV Download:** Enables users to download the user data as a CSV file.

## Installation

### Prerequisites

- Python 3.6 or higher
- MySQL server
- phpMyAdmin (optional, for easier database management)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/user-data-input-form.git
    cd user-data-input-form
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

### Using MySQL Command Line

1. **Create the MySQL database and table:**

    Ensure you have a MySQL server running and create a database named `user_data` and a table named `users` with the following schema:

    ```sql
    CREATE DATABASE user_data;

    USE user_data;

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        dob DATE NOT NULL
    );
    ```

### Using phpMyAdmin

1. **Access phpMyAdmin:**

    Open your web browser and go to `http://localhost/phpmyadmin` (or the appropriate URL for your phpMyAdmin installation).

2. **Create the database:**

    - Click on the "New" button in the left-hand sidebar.
    - Enter `user_data` as the database name and click "Create".

3. **Create the table:**

    - Select the `user_data` database from the left-hand sidebar.
    - Click on the "SQL" tab and enter the following SQL statement to create the `users` table:

    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        dob DATE NOT NULL
    );
    ```

    - Click "Go" to execute the statement.

## Running the Application

1. **Run the Streamlit application:**

    ```bash
    streamlit run mainapp.py
    ```

2. **Open the application in your web browser:**

    Streamlit will automatically open a new tab in your default web browser. If it doesn't, navigate to `http://localhost:8501` in your browser.

## Using the Application

### Input Form

- **Name:** Enter the user's name. Only letters and spaces are allowed.
- **Email:** Enter a valid email address.
- **Date of Birth:** Select the user's date of birth from the date picker.

After filling in the details, click the "Submit" button. The application will calculate the age based on the date of birth and insert the data into the database.

### Data Display

- The entered user data will be displayed in a table below the form.
- Each row in the table represents a user's data entry, showing the ID, Name, Email, Age, and Date of Birth.

### Delete User

- Each row in the table has a "Delete" button.
- Clicking the "Delete" button will remove the corresponding user entry from the database and refresh the table.

### Download Data

- Below the table, there is a "Download data as CSV" button.
- Clicking this button will download the user data in CSV format.

## Troubleshooting

- **Database Connection Issues:** Ensure your MySQL server is running and the connection details in the `create_connection` function are correct.
- **Dependency Issues:** Make sure all dependencies are installed correctly using the `pip install -r requirements.txt` command.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README provides a comprehensive guide to setting up, running, and using the Streamlit application. If you encounter any issues or have questions, feel free to open an issue in the repository or contact the maintainer.
