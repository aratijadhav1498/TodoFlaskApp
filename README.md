# 📝 Flask To-Do List Application

A simple and professional **To-Do List web application** built using **Python, Flask, HTML, CSS, and SQLite**.

This project demonstrates CRUD operations, database integration, task management, search functionality, and a responsive user interface.

---

## 🚀 Features

* ➕ Add new tasks
* 👀 View all tasks
* ✏️ Edit existing tasks
* 🗑️ Delete tasks
* ✅ Mark tasks as completed
* ⏳ Track task status
* 📅 Store task creation date and time
* 🔍 Search tasks
* ⭐ Set task priority
* 🎨 Dynamic priority and status styling
* 📱 Responsive design for smaller screens
* 💾 SQLite database for persistent data storage

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**

---

## 📂 Project Structure

```text
Flask-ToDo-List/
│
├── app.py
├── todo.db
│
├── templates/
│   ├── index.html
│   ├── add_task.html
│   └── edit_task.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Flask-ToDo-List
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 💾 Database

The application uses **SQLite** to store tasks.

Each task contains information such as:

* Task name
* Status
* Creation date and time
* Priority

The application performs CRUD operations directly with the SQLite database.

---

## 🔍 Search

Users can search for tasks using the search bar.

This makes it easier to find specific tasks when the task list becomes larger.

---

## ⭐ Task Priority

Tasks can be assigned different priority levels:

* 🔴 High
* 🟠 Medium
* 🟢 Low

The application dynamically changes the appearance of the priority badge based on the selected priority.

---

## 📱 Responsive Design

The interface is designed to adapt to smaller screen sizes using CSS media queries.

---

## 🎯 Learning Objectives

This project helped me practice:

* Python programming
* Flask web development
* Routing
* HTML templates
* Jinja2
* SQLite database operations
* CRUD operations
* Form handling
* Searching and filtering
* CSS styling
* Responsive web design

---

## 🔮 Future Improvements

Possible future enhancements include:

* User authentication and login
* Task categories
* Due dates and reminders
* Sorting and filtering
* Pagination
* REST API
* Deployment to a cloud platform

---

## 👩‍💻 Author

**Aarti**

Built as a Python and Flask portfolio project.
