# Definitie van de klasse.
class Student:
    def __init__(self, studentnr, naam):
        self.studentnr = studentnr
        self.naam = naam

# Een object maken van de klasse.
student1 = Student(101, "Jan Janssen")

# De gegevens van het object printen.
print(f"Studentnummer: {student1.studentnr}, Naam: {student1.naam}")