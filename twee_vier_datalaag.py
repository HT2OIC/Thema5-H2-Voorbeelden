# Klasse datalaag aanmaken.
class Datalaag:
    # Constructor met dictonary om de data op te slaan.
    def __init__(self):
        self.students = {}

    # Methode om data toe te voegen.
    def add_student(self, studentnr, student_data):
        """
            Voegt een nieuwe student toe aan de dictionary.
        """
        self.students[studentnr] = student_data

    # Methode om data op te halen.
    def get_students(self):
        """
            Geeft de volledige lijst van studenten terug.
            Returns: Lijst met studenten.
        """
        return self.students
    
    # Methode om de data van 1 student op te halen.
    def get_student(self, studentnr):
        """
            Zoekt een specifieke student op basis van het studentnummer.
            Returns: Gegevens 1 student.
        """
        return self.students.get(studentnr)  # Geeft None terug als het studentnummer niet bestaat