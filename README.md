# Inventory Manager

A web-based Inventory Management System built with **Flask** that allows users to securely manage their own inventory. Users can create an account, log in, and perform CRUD (Create, Read, Update, Delete) operations on their products.

## Features

* User Registration
* User Login & Logout
* Password Hashing for secure authentication
* Add Products
* Edit Products
* Delete Products
* Search Products
* User-specific inventory (each user only sees their own products)
* Responsive interface built with Bootstrap 5
* Flash messages for user feedback

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Flask-WTF
* WTForms
* Flask-Login
* Flask-Bootstrap
* Flask-CKEditor
* SQLite
* HTML
* Jinja2
* Bootstrap 5

## Project Structure

```text
inventory-manager/
│
├── app.py
├── models.py
├── forms.py
├── inventory.db
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── home.html
│   ├── add_product.html
│   ├── edit.html
│   ├── login.html
│   └── register.html
│
└── static/
```

## Installation

1. Clone the repository.

2. Create and activate a virtual environment.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## What I Learned

Building this project helped me gain practical experience with:

* Flask application structure
* SQLAlchemy models and relationships
* User authentication with Flask-Login
* Password hashing and security
* CRUD operations
* Search functionality
* WTForms form handling
* Jinja template inheritance and includes
* Bootstrap layout and responsive design
* Organizing a real-world Flask project

## Future Improvements

* Product categories
* Product images
* Pagination
* Dashboard statistics
* REST API
* Deployment to a cloud platform

## Author

**Emmanuel Adejumola**

Backend Developer (Python & Flask)
