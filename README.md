# 🎉 Event Management System

A full-stack **Event Management System** built with **Django**, **PostgreSQL**, **HTML**, and **Tailwind CSS**.  
This project uses **Django Class-Based Views (CBV)** and provides role-based features for **Admin**, **Manager**, and **Users**.

---

## 🚀 Features

### 🔐 Authentication
- Secure user registration & login
- Role-based access (Admin, Manager, User)

### 👨‍💻 Admin Features
- Manage (Add/Edit/Delete) Projects
- Manage Categories
- Manage Users

### 📂 Manager Features
- Personal Dashboard
- Monitor reservations on projects/events

### 👤 User Features
- User profile with editable information
- Reserve/Book projects or events
- Search events/projects by category, name, or date
- Ordering & filtering functionality

---

## 🛠️ Tech Stack
- **Backend**: Django (Python, Class-Based Views)
- **Frontend**: HTML, Tailwind CSS
- **Database**: PostgreSQL
- **Authentication**: Django Authentication System

---
## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Easin2050/Event-management.git
cd event-management
```
### 2️⃣ Create & activate a virtual environment
python -m venv venv_myenv

## Linux/Mac
source venv_myenv/bin/activate  
## Windows
venv_myenv\Scripts\activate  

### 3️⃣ Install dependencies   
pip install -r requirements.txt

### 4️⃣ Configure environment variables
SECRET_KEY=your-secret-key

DB_NAME=event_management

DB_USER=postgres

DB_PASSWORD=yourpassword

DB_HOST=localhost

DB_PORT=5432

### 5️⃣ Apply migrations
python manage.py migrate

### 6️⃣ Create a superuser
python manage.py createsuperuser

### 7️⃣ Run the server
python manage.py runserver

## 📜 License

This project is licensed under the **MIT License**.
