KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):

        if isinstance(kapasiteetti, int) and kapasiteetti > 0:
            self.kapasiteetti = kapasiteetti
        else:
            self.kapasiteetti = KAPASITEETTI

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm += 1
            return True

        elif not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            poistettavan_indeksi = self.lukujono.index(n)
            self.lukujono.remove(self.lukujono[poistettavan_indeksi])

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []

        for i in range(0, self.alkioiden_lkm):
            taulu.append(self.lukujono[i])

        return taulu

    def laskujen_alustus(self, a, b):
        lukujoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        return lukujoukko, a_taulu, b_taulu

    @staticmethod
    def yhdiste(a, b):
        lukujoukko, a_taulu, b_taulu = a.laskujen_alustus(a, b)

        for i in range(0, len(a_taulu)):
            lukujoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            lukujoukko.lisaa(b_taulu[i])

        return lukujoukko

    @staticmethod
    def leikkaus(a, b):
        lukujoukko, a_taulu, b_taulu = a.laskujen_alustus(a, b)

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    lukujoukko.lisaa(b_taulu[j])

        return lukujoukko

    @staticmethod
    def erotus(a, b):
        lukuJoukko, a_taulu, b_taulu = a.laskujen_alustus(a, b)

        for i in range(0, len(a_taulu)):
            lukuJoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            lukuJoukko.poista(b_taulu[i])

        return lukuJoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
