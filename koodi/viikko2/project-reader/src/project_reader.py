from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # muutetaan merkkijonomuotoinen sisältö dict-muotoon metodilla toml.loads
        parsed_toml = toml.loads(content)

        # haetaan sanakirjasta projektin nimi ja kuvaus (oletetaan, että tool ja poetry vakioita)
        test_name = parsed_toml["tool"]["poetry"].get("name")
        test_desc = parsed_toml["tool"]["poetry"].get("description")

        # haetaan sanakirjasta projektin riippuvuudet
        depend = parsed_toml["tool"]["poetry"].get("dependencies")
        dev_depend = parsed_toml["tool"]["poetry"].get("dev-dependencies")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(test_name, test_desc, depend, dev_depend)
