Django Todo Application

A task management web application built using Django that allows users to organize tasks efficiently using categories and status filters.

---

Features

- Create tasks
- Update existing tasks
- Delete tasks
- Mark tasks by status
- Create and delete categories
- Filter tasks by category
- Filter tasks by task status
- Bulk delete categories
- Success messages for user actions

---

Tech Stack

Backend:

- Python
- Django

Database:

- SQLite (development)

Frontend:

- HTML
- CSS
- BOOTSTRAP
- Django Template Language

---

Project Structure

todo_project/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── todo_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
├── static/
└── db.sqlite3

---

How to Run Locally

1. Clone the repository

git clone https://github.com/Nkiruthika2541/TODO---Django.git

2. Navigate to the project directory

cd todo-app

3. Create virtual environment

python -m venv venv

4. Activate the virtual environment

source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

6. Run migrations

python manage.py migrate

7. Start the development server

python manage.py runserver

---

Future Improvements

- Add pagination for task lists
- Add search functionality
- Improve UI with Bootstrap
- Add user authentication
- Deploy to cloud hosting

---

Live Demo
https://simple-todo-app-aq60.onrender.com/todo/home/

Author

Kiruthika P
Backend Developer (Django)