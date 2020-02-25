

class Catalog:

    def __init__(self):
        self.set_nume_profesor()
        self.nume_profesor = self.get_nume_profesor()
        self.set_numar_elevi()
        self.numar_elevei = self.get_numar_elevi()
        self.set_clasa()
        self.clasa = self.get_clasa()
        self.set_an_calendaristic()
        self.an_calendaristic = self.get_an_calendaristic()

    def get_nume_profesor(self):
        return self.nume_profesor

    def set_nume_profesor(self):
        self.nume_profesor = input("Nume complet profesor? = ")

    def get_numar_elevi(self):
        return self.numar_elevei

    def set_numar_elevi(self):
        self.numar_elevei = input("Numar elevi? = ")

    def get_clasa(self):
        return self.clasa

    def set_clasa(self):
        self.clasa = input("Clasa? = ")

    def get_an_calendaristic(self):
        return self.an_calendaristic

    def set_an_calendaristic(self):
        self.an_calendaristic = input("An calendaristic? = ")

class Elev:

    def __init__(self, nume_elev, prenume_elev):
        self.nume_elev = nume_elev
        self.prenume_elev = prenume_elev

class SituatieElev:

    def e_prezent(self):
        self.prezent = input("Prezent (1) / Absent (0) ? = ")
        if self.prezent == 1:
            prezent = 1
            return True
        else:
            prezent = 0
            return False

    def a_absolvit(self):
        self.absolvent = input("A absolvit? da/nu ? = ")
        if self.absolvent == "da" or "Da":
            self.absolvent = 1
            return True
        else:
            self.absolvent = 0
            return False
    def get_prezenta(self):
        return self.prezent

print("Introdu date despre catalog: ")
catalogCinar = Catalog()

print("Profesor = " + str(catalogCinar.nume_profesor) +
      "\nNumar elevi= " + str(catalogCinar.numar_elevei) +
      "\nClasa= " + str(catalogCinar.clasa) +
      "\nAn calendaristic= " + str(catalogCinar.an_calendaristic))

# catalogCinar2 = Catalog()
nr_elevi = (input("Cati elevi doresti sa introduci? = "))
nr_elevi = int(nr_elevi)
situatieElev = SituatieElev()
listaElevi = []
for i in range(nr_elevi):

    elev = Elev(input("Numele Elevului? = "), input("Prenumele Elevului? = "))



    situatieElev.e_prezent()
    situatieElev.a_absolvit()
    listaElevi.append(elev)

for i in range (len(listaElevi)):
    print("Elevul " + str(i+1) + " se numeste: " + str(listaElevi[i].nume_elev) + " " + str(listaElevi[i].prenume_elev))


print("SomeChangesmadeHere")
# print(situatieElev.get_prezenta())


# situatieElev2 = SituatieElev()

