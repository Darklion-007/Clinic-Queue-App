from flask import Flask, render_template, request, redirect
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
        name = request.form["name"]
        patient = Patient(name)
        clinic.add_patient(patient)
        return redirect("/")
    return render_template("add_patient.html")

@app.route("/next")
def next_patient():
    clinic.see_patient()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)