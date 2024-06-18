# SQL Injection Demonstration Website

This simple web application that demonstrates the power of SQL injection attacks and how to prevent them.

## Overview

The application features a basic login functionality with two buttons:
- **Vulnerable Login**: Naive login method without any mitigation for SQL injection attacks.
- **Secured Login**: Uses parameterized queries to prevent SQL injection.

A simple SQLite database is initialized with a single user:
- **Username**: admin
- **Password**: 1234

## How to perform the SQL Injection

When using the **Vulnerable Login** button, you can perform an SQL injection using the following credentials:

- **Username**: `' OR 1=1--`
- **Password**: can be anything as it is ignored due to the `--` comment in the username field.

The above credentials exploit the SQL injection vulnerability by altering the SQL query to always return a true condition, effectively bypassing authentication.

## Secured login demonstration

Attempting the same SQL injection input with the **Secured Login** button will not work.  
This button uses parameterized queries, which treat user input as data, not executable code, preventing the alteration of the SQL query.


## Technologies used

- **Flask**: To build the web application.
- **SQLite**: For creating a simple database to store user credentials.