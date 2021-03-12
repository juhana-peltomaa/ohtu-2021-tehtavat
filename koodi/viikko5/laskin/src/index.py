import tkinter as tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():
    sovellus = Sovelluslogiikka()

    window = tk.Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window)
    kayttoliittyma.kaynnista()

    window.mainloop()


if __name__ == "__main__":
    main()
