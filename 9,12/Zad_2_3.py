
class Człowiek:
    def __init__(self, imie, nazwisko, wiek, płeć, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.płeć = płeć
        self.wzrost = wzrost
        self.waga = waga
        self.okupacja = None
    def obudzsie(self):
        print(f"{self.imie} {self.nazwisko} budzi się")
    def zjedz(self, coje):
        print(f"{self.imie} {self.nazwisko} je {coje}")
    def idzdo(self, miejsce):
        return f"{self.imie} {self.nazwisko} idz do {miejsce}"
    def spij(self):
        print(f"{self.imie} {self.nazwisko} idzie spać")
    def __str__ (self):
        return f"[{self.płeć}] {self.imie} {self.nazwisko} ({self.wiek}): waga: {self.waga}, wzrost: {self.wzrost}, okupacja: {self.okupacja}"
    

class Student(Człowiek):
        retutn f"{self.okupacja} {self.imie} {self.nazwisko} studiuje {kierunek}"
    def pije(self.)


    if __name__ == '__main__':
        student = Student('Kuba', 'Król', 20 'menszczyzna' 179 60)
        doktkor = Wykładowca('Marek', 'Kosa', 69 'MĘŻCZYZNA' 173 100)
        from time import sleep
        doktor