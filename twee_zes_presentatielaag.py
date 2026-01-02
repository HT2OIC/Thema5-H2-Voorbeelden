# Klasse Datalaag en Domeinlogica importeren van hun code.
from twee_vier_datalaag import Datalaag
from twee_vijf_domeinlogica import Domeinlogica

# Klasse Presentatielaag aanmaken.
class Presentatielaag:
    # Constructor die een instantie van de domeinlogica aanmaakt.
    # Gelijktijdige gebruikers hebben afzonderlijke instanties om met de domeinlogica te communiceren.
    def __init__(self, domeinlogica):
        self.domeinlogica = domeinlogica

    # Opbouw interface.
    def show_menu(self):
        """Toont het hoofdmenu en verwerkt de invoer van de gebruiker."""
        # Continu keuzemenu laten zien, tenzij het programma wordt afgesloten.
        while True:
            print("\nKlassenlijst Beheer")
            print("1. Student toevoegen")
            print("2. Klassenlijst bekijken")
            print("3. Afsluiten")
            # O.b.v. input gebruiker de juiste methode oproepen.
            choice = input("Maak een keuze: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                print("Programma beëindigd.")
                break
            else:
                print("Ongeldige keuze, probeer opnieuw.")
    
    # Methode om nieuwe data op te slaan.
    def add_student(self):
        """Laat de gebruiker een nieuwe student toevoegen."""
        # Vragen naar de nodige input van de gebruiker.
        naam = input("Voer de naam van de student in: ")
        studentnr = input("Voer het studentnummer in: ")
        klas = input("Voer de klas in: ")

        # Fout/succes bepalen met behulp van foutencontrole domeinlogica.
        if self.domeinlogica.add_new_student(naam, studentnr, klas):
            print(f"Student {naam} succesvol toegevoegd.")
        else:
            print(f"Fout: Studentnummer {studentnr} bestaat al!")

    # Methode om data op te halen.
    def view_students(self):
        """Laat de gebruiker de klassenlijst bekijken."""
        students = self.domeinlogica.list_students()

        # Klassenlijst tonen als er data aanwezig is.
        if students:
            print("\nKlassenlijst:")
            for studentnr, data in students.items():
                print(f"Studentnr: {studentnr}, Naam: {data['naam']}, Klas: {data['klas']}")
        else:
            print("De klassenlijst is leeg.")

# Het programma starten gekoppeld aan de verschillende lagen.
if __name__ == "__main__":
    datalaag = Datalaag()
    domeinlogica = Domeinlogica(datalaag)
    Presentatie_laag = Presentatielaag(domeinlogica)
    Presentatie_laag.show_menu()