class FIFO:
    def __init__(self):
        self.elementy = []

    def jesli_pusta(self):
        return len(self.elementy) == 0

    def zakolejkuj(self, item):
        self.elementy.append(item)

    def wyciagnij(self):
        if self.jesli_pusta():
            return None
        else:
            return self.elementy.pop(0)