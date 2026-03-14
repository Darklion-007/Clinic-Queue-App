from flask import Flask, render_template, request, redirect, url_for
from models import Patient, ClinicQueue

app = Flask(__name__)

clinic = ClinicQueue()

@app.route("/")
def home():
    return render_template(
        "index.html",
        queue=clinic.queue,
        total_seen=clinic.total_seen
    )

@app.route("/add", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:  # Validate that name is not empty
            patient = Patient(name)
            clinic.add_patient(patient)
            return redirect(url_for("home"))
        else:
            # Optionally, you can handle the case where name is empty
            # For example, re-render the form with an error message
            return render_template("add_patient.html", error="Please enter a valid name.")
    return render_template("add_patient.html")

@app.route("/next")
def next_patient():
    clinic.see_patient()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)