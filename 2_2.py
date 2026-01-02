# Definitie van de klasse.
class Student:
    def __init__(self, studentnr, naam, klas):
        self.studentnr = studentnr
        self.naam = naam
        self.klas = klas

# Een object maken van de klasse.
student1 = Student(101, "Jan Janssen", "H61IC")

# De gegevens van het object printen.
print(f"Studentnummer: {student1.studentnr}, Naam: {student1.naam}, Klas: {student1.klas}")