# Online Examination System

A web-based examination portal built with **Django**, supporting three roles — **Admin**, **Teacher**, and **Student** — for managing courses, questions, and online tests with automatic result evaluation.

## Features

### Admin
- Central dashboard showing total students, teachers, courses, and questions
- Approve or reject teacher signup requests
- View, update, and delete teacher and student records
- Manage teacher salaries
- Create and manage courses (with number of questions and total marks per course)
- Add, view, and delete questions (multiple-choice, with 4 options and a correct answer) for each course
- View and check student marks/results per course

### Teacher
- Register and wait for admin approval before accessing the portal
- View assigned salary and profile details

### Student
- Register and log in to attempt available course exams
- Objective (MCQ) based online tests
- Automatic marks calculation and result storage after submission

### Other
- Contact Us page that sends messages to the site admin's email via Gmail SMTP
- Role-based authentication using Django's built-in `auth` app and user groups (`TEACHER`, `STUDENT`)

## Tech Stack

- **Backend:** Python, Django 3.0.5
- **Database:** SQLite3 (default, included as `db.sqlite3`)
- **Frontend:** Django Templates, HTML/CSS
- **Other libraries:** `django-widget-tweaks` (form field styling), `Pillow` (image/profile picture handling)

## Project Structure

```
onlinexamination/
├── onlinexam/          # Project settings, root URLs, WSGI/ASGI config
├── exam/                # Core app: courses, questions, results, admin views
│   ├── models.py         # Course, Question, Result models
│   ├── forms.py          # Contact us, course, question forms
│   └── views.py          # Admin-side and shared views/logic
├── teacher/              # Teacher app (profile, approval, salary) — referenced in
│                          # settings/urls; not included in this archive, add separately
├── student/              # Student app (registration, dashboard, exam attempt)
│   ├── forms.py
│   └── admin.py
├── static/
│   ├── image/            # Role selection icons (admin/teacher/student)
│   └── profile_pic/      # Uploaded teacher/student profile pictures
├── manage.py
├── requirements.txt
└── db.sqlite3
```

> **Note:** This archive is missing a few pieces referenced by the project — the `teacher` app's Python files, `student/models.py` / `student/urls.py` / `student/views.py`, and the HTML `templates/` folders for all apps. Django's `INSTALLED_APPS` and `urls.py` do reference a `teacher` app, so you'll need to add these back (from your original source or version control) before the project will run correctly.

## Getting Started

### Prerequisites
- Python 3.7+ installed
- `pip` package manager

### Installation

1. **Clone/extract the project** and move into the project folder:
   ```bash
   cd onlinexamination
   ```

2. **(Recommended) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an admin (superuser) account:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. Open your browser at `http://127.0.0.1:8000/` and log in as admin at `/adminlogin` using your superuser credentials.

### Email Configuration (Contact Us page)

The Contact Us feature sends email via Gmail SMTP. Update the following in `onlinexam/settings.py` with your own credentials before using it:

```python
EMAIL_HOST_USER = 'from@gmail.com'          # sender email
EMAIL_HOST_PASSWORD = 'ENTER_PASSWORD'      # sender email's app password
EMAIL_RECEIVING_USER = ['to@gmail.com']     # where contact messages are delivered
```

> Gmail now requires an **App Password** (with 2-Step Verification enabled) rather than your regular account password, since Google has discontinued "less secure app access."

## Usage Flow

1. **Admin** logs in, creates courses (name, number of questions, total marks), and adds MCQ questions to each course.
2. **Teachers** register and wait for admin approval; admin can view pending/approved teachers and manage salaries.
3. **Students** register, log in, and attempt available course exams.
4. On submission, the system automatically calculates and stores the student's marks (`Result` model), which the admin can review.

## License

See the `LICENSE` file included in the project.

## Credits

Developed by **Ambikesh Kumar**.