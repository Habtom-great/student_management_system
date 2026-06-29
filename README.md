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

templates
│
├── base.html
│
├── dashboard
│   ├── home.html
│   ├── admin_dashboard.html
│   └── charts.html
│
├── students
│   ├── student_dashboard.html
│   ├── student_list.html
│   ├── student_form.html
│   └── student_detail.html
│
├── instructors
│   ├── instructor_dashboard.html
│   ├── instructor_list.html
│   └── instructor_detail.html
│
└── courses
    ├── courses_dashboard.html
    ├── course_list.html
    └── course_detail.html