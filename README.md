# SQL injection demo website  

A simple database is created with a single user called admin and password of 1234.

When using the `vulnrable login` button, we can construct the following SQL injection:    
username = `'OR 1=1--`    
password = whatever  

however, when clicking on the `secured login` button, this wont work anymore since we are using parametrized queries.

Developed using Flask.

# SQL Injection Demonstration Website

This simple web application demonstrates the power of SQL injection attacks and how to prevent it.

## Overview

The application features a basic login functionality with two buttons:
- **Vulnerable Login**: Naive login method without any mitigation for SQL injection attacks.
- **Secured Login**: Uses parameterized queries to prevent SQL injection.

A simple SQLite database is initialized with a single user:
- **Username**: admin
- **Password**: 1234

## Technologies Used

- **Flask**: To build the web application.
- **SQLite**: For creating a simple database to store user credentials.

## How to Perform SQL Injection

When using the **Vulnerable Login** button, you can perform an SQL injection using the following credentials:

- **Username**: `' OR 1=1--`
- **Password**: can be anything as it is ignored due to the `--` comment in the usename

The above credentials exploit the SQL injection vulnerability by altering the SQL query to always return a true condition, effectively bypassing authentication.

## Secured Login Demonstration

Attempting the same SQL injection input with the **Secured Login** button will not work.  
This button uses parameterized queries, which treat user input as data, not executable code, preventing the alteration of the SQL query.