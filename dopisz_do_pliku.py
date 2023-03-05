def dopisz_do_pliku(tekst):
    with open("plik.txt", "a") as f:
        f.write(tekst + "\n")