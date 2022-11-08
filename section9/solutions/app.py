from flask import Flask, render_template, request
from cs50 import SQL

db = SQL("sqlite:///users.db")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cat")
def cat():
    return "You are on the Cat Page!"

@app.route("/welcome/<name>")
def welcome(name):
    db.execute("INSERT INTO users VALUES (?)", name)
    users = db.execute("SELECT * FROM users")
    # The below line uses Pthon's list comprehension, but it is the equivalen of writing:
    # temp_users = []
    # for row in users:
    #     temp_users.append(row["name"])
    # users = temp_users
    users = [row["name"] for row in users]
    return render_template(
        "welcome.html",
        x=name,
        users=users
    )

@app.route("/welcome2")
def welcome2():
    name = request.args.get("q")
    return f"Welcome, {name}"

@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        mood = request.form.get("mood")
        age = request.form.get("age")
        return f"Your mood is {mood} and you are {age} years old."
    else:
        return render_template("survey.html")