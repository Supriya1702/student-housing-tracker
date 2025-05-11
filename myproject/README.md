
# Django Project Setup Guide  

This guide provides step-by-step instructions for setting up a Django project on your local machine.  

## Prerequisites  

Ensure you have the following installed on your system:  
- Python (>=3.8) – [Download here](https://www.python.org/downloads/)  
- pip (Python package manager) – Comes with Python  
- Virtual environment (`venv`)  
- PostgreSQL/MySQL (Optional, for production databases)  

## 1. Setting Up the Django Project  

### Step 1: Create a Virtual Environment  
Run the following commands in your terminal:  

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Django  
Once the virtual environment is activated, install Django:  

```sh
pip install django
```

Verify the installation:  

```sh
django-admin --version
```

### Step 3: Create a New Django Project  

```sh
django-admin startproject myproject
cd myproject
```

### Step 4: Run the Development Server  

```sh
python manage.py runserver
```

Open your browser and go to:  
👉 `http://127.0.0.1:8000/`  

## 2. Project Structure  

```
myproject/
│── manage.py          # Django management script
│── myproject/         # Main project folder
│   ├── __init__.py    # Marks directory as a Python package
│   ├── settings.py    # Project settings
│   ├── urls.py        # URL routing
│   ├── asgi.py        # ASGI configuration
│   ├── wsgi.py        # WSGI configuration
│── app/               # Django app (to be created)
```

## 3. Creating a Django App  

Inside your project, create an app named `api`:  

```sh
python manage.py startapp api
```

Add the app to `INSTALLED_APPS` in `settings.py`:  

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # Newly added app
]
```

## 4. Database Setup (Optional)  

If you're using PostgreSQL, install `psycopg2`:  

```sh
pip install psycopg2-binary
```

Modify `settings.py`:  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Run database migrations:  

```sh
python manage.py migrate
```

## 5. Creating a Superuser  

To access the Django admin panel, create a superuser:  

```sh
python manage.py createsuperuser
```

Then, log in at `http://127.0.0.1:8000/admin/`.  

## 6. Running the Project  

Use the following command to start the development server:  

```sh
python manage.py runserver
```

## 7. Additional Setup  

### Install Additional Dependencies  

```sh
pip install djangorestframework  # For APIs
pip install django-cors-headers   # If using React frontend
```

### Setup Static Files  

Run the command:  

```sh
python manage.py collectstatic
```

## 8. Deploying Django  

For production, use:  

```sh
pip install gunicorn
gunicorn myproject.wsgi
```

Or use `Docker` for containerization.  

