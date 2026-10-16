# Flask To-Do List Application

A task management web application built using Python, Flask, and SQLite. It allows users to organize daily tasks through a simple, professional interface.

## Features

- **Create Tasks:** Add new tasks to your list.
- **Update Tasks:** Edit existing task details.
- **Delete Tasks:** Remove tasks when they are no longer needed.
- **Task Status:** Mark tasks as Pending or Completed.
- **Task Priority:** Assign Low, Medium, or High priority.
- **Date and Time:** Record when tasks are created.
- **Search Tasks:** Find tasks using the search feature.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
TodoFlaskApp/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

*Note: Your templates folder may contain additional HTML files.*

## How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/aratijadhav1498/TodoFlaskApp.git

   ```

2. Open the project folder:

   ```bash
   cd TodoFlaskApp
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install Flask:

   ```bash
   pip install Flask
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open the local address displayed in the terminal, usually `http://127.0.0.1:5000/`.

## Learning Outcomes

This project demonstrates practical experience with Flask routing, CRUD operations, SQLite database integration, HTML forms, task filtering, and Git-based version control.

## Future Improvements

- User registration and login
- Deployment to a public hosting platform
- REST API endpoints
- Automated tests

