from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_registered = datetime.now()

    def display(self):
        return f"{self.name} - {self.time_registered.strftime('%H:%M:%S')}"

class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.total_seen = 0

    def add_patient(self, patient):
        self.queue.append(patient)

    def see_patient(self):
        if self.queue:
            patient = self.queue.pop(0)
            self.total_seen += 1
            return patient
        return None