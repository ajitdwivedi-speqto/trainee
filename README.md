# Speqto - Learning Projects Repository 📚

A comprehensive collection of Django web development projects demonstrating various concepts from basic CRUD operations to advanced API development with JWT authentication, REST frameworks.

## 📁 Projects Overview

This repository contains **2 main projects** and one Simple I/o file handling and one simple Django setup project:

### 1. **demoproject** 🟢
**Type:** Django Web Application  
**Description:** Django application with basic templates and models, Media file setup

### 2. **crudapp** 🟡 
**Type:** Django REST API with JWT Authentication  
**Description:** REST API with user authentication, JWT tokens, and Swagger documentation

### 4. **ecommerce** 🔴 
**Type:** Django Application  
**Description:** REST API with user authentication, JWT tokens, and Swagger documentation, API error-handling

---

### Prerequisites
- Python 3.8+ installed
- PostgreSQL database running
- Virtual environment activated

### Global Setup

# 1. Create and activate virtual environment
# 2. Install dependencies (if not already installed)
pip install -r ../crudapp/requirements.txt
```

### Run Any Project

# Navigate to project folder in terminal
cd crudapp              # or demoproject, ecommerce

# Create database tables
python manage.py migrate

# Create superuser (for admin panel)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access at http://localhost:8000
```
---

## Technologies Used
- **Framework:** Django 5.2.8
- **Database:** PostgreSQL (configured in all projects)
- **ORM:** Django ORM
- **API Framework:** Django REST Framework (DRF)
- **Documentation:** drf-yasg (Swagger/OpenAPI)
- **Authentication:** JWT (Simple JWT)
- **CORS:** django-cors-headers

### Additional Tools
- **Email:** SMTP with Gmail
- **File Upload:** Pillow (image processing)
- **API Docs:** Swagger UI, ReDoc
- **Middleware:** Custom request logging, CORS handling


---
## 🔐 Environment Configuration

Create a `.env` file in each project root:

```env
# Database
DB_NAME=project_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Email (for ecommerce)
EMAIL_HOST_USER=your_gmail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

---

## 📝 File Structure

```
speqto/
├── README.md                    ← You are here (Global Guide)
├── .git/                        ← Version control
├── .gitignore                   ← Git ignore rules
│
├── trainee/                     ← Virtual environment
│   ├── Scripts/
│   └── Lib/
│
├── input_output/
│   └── input_output.py          ← Python script
│
├── demoproject/                 ← Demo Django app
│   ├── manage.py
│   ├── README.md                ← Project specific README
│   ├── requirements.txt
│   └── ...
│
├── crudapp/                     ← Main REST API
│   ├── manage.py
│   ├── README.md                ← CRUD App
│   ├── requirements.txt
│   ├── crudapp/                 ← Project config
│   ├── student_teacher/         ← Student app (API)
│   ├── authapp/                 ← Auth app (JWT)
│   └── ...
│
└── ecommerce/                   ← E-commerce
    ├── manage.py
    ├── README.md                ← E-commerce project specific README
    ├── requirements.txt
    ├── ecom/                    ← Main app
    ├── utils/                   ← Helpers
    └── ...
