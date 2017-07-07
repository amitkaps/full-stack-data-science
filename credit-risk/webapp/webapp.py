from flask import Flask, render_template, redirect
from forms import LoanForm
import datetime
import pathlib
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abrakadabra'

def get_loans():
    path = pathlib.Path("loans")
    path.mkdir(exist_ok=True)

    loans = []
    for p in path.glob("*.loan"):
        loan = json.loads(p.read_text(encoding='utf-8'))
        loans.append(loan)
    return loans

def save_loan(**fields):
    root = pathlib.Path("loans")
    root.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().isoformat()
    fields['timestamp'] = timestamp
    path = root.joinpath(timestamp + ".loan")
    path.write_text(json.dumps(fields))
    print("Saved loan", path)

@app.route("/", methods=["GET", "POST"])
def index():
    form = LoanForm()
    if form.validate_on_submit():
        save_loan(
            amount=form.amount.data,
            duration=form.duration.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            income=form.income.data,
            ownership=form.ownership.data)
        return redirect("/")
    return render_template("index.html", form=form)

@app.route("/admin")
def admin():
    loans = get_loans()
    return render_template("admin.html", loans=loans)

if __name__ == "__main__":
    app.run()
