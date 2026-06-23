# 🎓 Student Management System (Django LMS)

A full-featured Learning Management System built with Django.

---

## 🚀 Features

- Student registration and management
- Instructor management system
- Course creation and enrollment
- Admin dashboard
- Authentication system (login/logout)
- Role-based access (Student / Instructor / Admin)
- File upload support (assignments, materials)

---

## 🛠 Tech Stack

- Python 3.9+
- Django
- SQLite (dev)
- HTML, CSS, Bootstrap
- JavaScript

---

## 📦 Installation

```bash
git clone https://github.com/Habtom-great/student_management_system.git
cd student_management_system

python -m venv venv
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver