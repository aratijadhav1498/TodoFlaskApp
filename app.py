from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task TEXT NOT NULL )
        """)

    conn.commit()
    conn.close()



#READ
@app.route("/")
def home():
    search = request.args.get("Search", "")

    conn = get_db_connection()

    if search:
        tasks = conn.execute(
            "SELECT * FROM tasks WHERE task LIKE ?",
            ("%" + search + "%",)
        ).fetchall()
    else:
        tasks = conn.execute(
            "SELECT * FROM tasks"
        ).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)


#CREATE
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":

        print("FORM DATA:", request.form)

        task = request.form["task"].strip()

        priority = request.form.get("priority","Medium")
        print("SELECTED PRIORITY:", priority)

        if not task:
            return "Please enter a task."

        conn = get_db_connection()

        conn.execute(

            "INSERT INTO tasks (task, status, created_at, priority) VALUES (?, ?, ?, ?)",
            (task, "Pending",
             datetime.now().strftime("%d-%m-%Y %I:%M %p"),
             priority
             )
        )

        conn.commit()
        conn.close()

        return redirect("/")
    return render_template("add_task.html")


#DELETE
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = get_db_connection()

    conn.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Completed", task_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")

#UPDATE
@app.route("/edit/<int:task_id>", methods=["GET","POST"])
def edit_task(task_id):

    conn = get_db_connection()

    if request.method == "POST":

        new_task = request.form["task"].strip()

        if not new_task:
            conn.close()
            return "Task cannot be empty."

        conn.execute(
           "UPDATE tasks SET task = ? WHERE id = ?",
           (new_task, task_id)
       )

        conn.commit()
        conn.close()

        return redirect("/")

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close() 

    return render_template(
        "edit_task.html",
        task=task

    )


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)


