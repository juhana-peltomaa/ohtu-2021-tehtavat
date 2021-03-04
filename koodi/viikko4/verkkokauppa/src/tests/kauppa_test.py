import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = pankki_mock = Mock()
        self.viitegeneraattori_mock = viitegeneraattori_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

            elif tuote_id == 2:
                return Tuote(2, "kahvi", 10)

            elif tuote_id == 3:
                return Tuote(3, "kalja", 15)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_metodeilla(self):

        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 lisätään, tällöin:
        hinta = 5

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_metodeilla_kahdelle__eri_tuotteelle(self):

        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 ja 2 lisätään, tällöin:
        hinta = 15

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_metodeilla_kahdelle_samalle_tuotteelle(self):

        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 lisätään kaksi kertaa tällöin:
        hinta = 10

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_metodeilla_loppuneelle_tuotteelle(self):
        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 lisätään ja tällöin:
        hinta = 5

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)

    def test_asiointi_nollaa_edellisen_ostoskorin(self):
        kauppa = self.kauppa

        # tehdään ostokset ja nollataan välissä
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)

        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 lisätään ja tällöin:
        hinta = 10

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)

    def test_uusi_viitenumero_jokaiselle_maksutapahtumille(self):
        kauppa = self.kauppa

        # tehdään ostokset ja nollataan välissä
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)

        kauppa.tilimaksu("kari", "12345")

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)

        kauppa.tilimaksu("kari", "12345")

        # varmistetaan, että maksutapahtumat kutsuvat uutta viitenumeroa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_poisto_ostoskorista_toimii(self):
        kauppa = self.kauppa

        # tehdään ostokset ja nollataan välissä
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)

        kauppa.poista_korista(1)
        kauppa.lisaa_koriin(2)

        kauppa.tilimaksu("pekka", "12345")

        # tässä tapauksessa ainoastaan tuote 1 lisätään ja tällöin:
        hinta = 10

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla metodeilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", hinta)
