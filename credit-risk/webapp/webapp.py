from flask import Flask, render_template, redirect
from forms import LoanForm
import loansdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abrakadabra'

@app.route("/", methods=["GET", "POST"])
def index():
    form = LoanForm()
    if form.validate_on_submit():
        loansdb.save_loan(
            amount=form.amount.data,
            duration=form.duration.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            income=form.income.data,
            ownership=form.ownership.data)
        return render_template("thankyou.html", name=form.name.data)
    return render_template("index.html", form=form)

@app.route("/admin")
def admin():
    loans = loansdb.get_loans()
    return render_template("admin.html", loans=loans)

if __name__ == "__main__":
    app.run()
