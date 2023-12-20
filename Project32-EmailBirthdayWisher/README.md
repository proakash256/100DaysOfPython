# Email Birthday Wisher

## Introduction
The provided Python script represents an Email Birthday Wisher program designed to automatically send birthday wishes via email to individuals listed in a CSV file (`birthdays.csv`). The script uses the `smtplib` library for email communication, `pandas` for handling CSV data, and includes random letter templates for personalized birthday messages. The documentation outlines the features, Python concepts used, and the structure of the code.

## Features

### Birthday Email Sending
- The program reads a CSV file (`birthdays.csv`) containing information about individuals, including their names, email addresses, and birthdays.
- It checks if there are any birthdays today (`TODAY`), and if so, it selects a random letter template and sends a personalized birthday email using the Gmail SMTP server.

### Personalized Letter Templates
- The program includes multiple letter templates stored in the `letter_templates` directory.
- A random letter template is selected for each birthday to add variety to the birthday wishes.

### SMTP Email Sending
- The `smtplib` library is used to establish a connection with the Gmail SMTP server.
- The connection is secured using TLS, and the user's email and password are used for authentication.
- The birthday email is sent with a subject line of "Happy Birthday!!" and the personalized letter content.

## Python Concepts Used

- **Datetime (datetime module):** Utilized to get the current month and day for checking birthdays.
- **File Handling (`open`):** Reads the content of letter templates from text files.
- **Randomization (`random` module):** Selects a random letter template for each birthday.
- **Email Sending (`smtplib`):** Establishes an SMTP connection and sends emails.
- **Data Processing (pandas):** Reads and processes data from a CSV file (`birthdays.csv`).
- **String Manipulation:** Replaces placeholders in the letter templates with the birthday individual's name.
- **Error Handling (`try`, `except`):** Handles potential exceptions such as file reading errors or SMTP connection errors.

## Code Structure

The code is organized into several sections:

1. **Initialization:** Defines constants for the user's email and password, and the current date (`TODAY`).
2. **Data Loading:** Reads birthday data from the CSV file and creates a dictionary for easy access.
3. **Birthday Email Sending:** Checks if there are birthdays today and sends personalized emails.
4. **Letter Templates:** Reads random letter templates and replaces placeholders with the individual's name.
5. **SMTP Connection:** Establishes a connection with the Gmail SMTP server, logs in, and sends the birthday email.

## Conclusion

The Email Birthday Wisher program automates the process of sending personalized birthday wishes via email. It combines Python concepts such as datetime handling, file reading, email communication, and data processing to create a tool that can be scheduled to run daily, ensuring that birthday wishes are sent promptly. The use of random letter templates adds an element of surprise and personalization to the birthday messages, creating a delightful experience for the recipients.
