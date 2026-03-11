# Product Catalog Django Web App

## Overview
This is a simple Django web application for a Product Catalog, built for COGS 185 Homework 5. It allows users to add items and view a list of all items in the catalog. The app uses ModelForms, Bootstrap for styling, and follows Django best practices.

## Features
- Add new items with name, serial number (unique), quantity, expiry date, and optional notes
- List all items, sorted by newest first
- Bootstrap-styled UI
- Navigation between Add and List pages

## Setup Instructions

### 1. Clone the repository or unzip the project folder

### 2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django
```
pip install django
```

### 4. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```

### 6. Run the development server
```
python manage.py runserver
```

### 7. Access the app
- Add Item: http://127.0.0.1:8000/add/
- List Items: http://127.0.0.1:8000/items/
- Admin: http://127.0.0.1:8000/admin/

## Adding Dummy Data
You can add at least 5 items using the Django admin or the shell:
```
python manage.py shell
```
Then run:
```
from catalog.models import Item
Item.objects.create(name='Item 1', serial_number='SN001', quantity=10, expiry_date='2026-12-31')
Item.objects.create(name='Item 2', serial_number='SN002', quantity=5, expiry_date='2026-11-30')
Item.objects.create(name='Item 3', serial_number='SN003', quantity=7, expiry_date='2027-01-15')
Item.objects.create(name='Item 4', serial_number='SN004', quantity=2, expiry_date='2026-10-10')
Item.objects.create(name='Item 5', serial_number='SN005', quantity=20, expiry_date='2027-03-01')
```

## Debugging
- If you encounter errors, check the terminal output and follow the error messages.
- For validation errors (e.g., duplicate serial number, negative quantity), the form will display error messages.

## LLM Used
- GitHub Copilot (GPT-4.1)

## License
MIT
