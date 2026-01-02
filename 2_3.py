# Definitie van de klasse.
class Student:
    def __init__(self, studentnr, naam, klas):
        self.studentnr = studentnr
        self.naam = naam
        self.klas = klas
    
    def beschrijving(self):
        return f"Studentnummer: {self.studentnr}, Naam: {self.naam}, Klas: {self.klas}"

# Methode gebruiken
student3 = Student("Alice Brown", 103, "5B")
print(student3.beschrijving())