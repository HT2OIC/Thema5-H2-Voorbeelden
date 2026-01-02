# Klasse Datalaag importeren van de datalaagcode.
from twee_vier_datalaag import Datalaag

# Klasse domeinlogica aanmaken.
class Domeinlogica:
    # We maken een instantie van de datalaag aan.
    # Gelijktijdige gebruikers hebben afzonderlijke instanties om met de datalaag te communiceren.
    def __init__(self, datalaag):
        self.datalaag = datalaag
    
    # Methode om nieuwe student toe te voegen. We roepen de methode uit de datalaag op.
    # Hier gebeurt ook de foutencontrole.
    def add_new_student(self, naam, studentnr, klas):
        """
            Voegt een nieuwe student toe als het studentnummer uniek is.
            Returns:   
                Boolean: Student toevoegen gelukt/niet gelukt.
        """
        if self.datalaag.get_student(studentnr) is None:
            self.datalaag.add_student(studentnr, {"naam": naam, "klas": klas})
            return True
        else:
            return False
    
# Methode om data op te halen. We roepen de methode uit de datalaag op.
    def list_students(self):
        """
            Geeft de volledige lijst van studenten terug.
            Returns:
                Lijst met studentengegevens.
        """
        return self.datalaag.get_students()