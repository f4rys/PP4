class Zajecia:
    def __init__(self, liczba_studentow):
        self.liczba_studentow = liczba_studentow

    def zapisz_studenta(self):
        if(self.liczba_studentow < 10):
            self.liczba_studentow = self.liczba_studentow + 1
        else:
            print("Osiągnięto maksymalną liczbę studentów na zajęciach.")
