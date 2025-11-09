
from datetime import datetime
import itertools

class CompteBancaire:
    _compteur_id = itertools.count(1)  

    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        self.id_compte = next(CompteBancaire._compteur_id)
        self._operations = []  
    def deposer(self, montant):
        """Dépose un montant positif et ajoute à l'historique."""
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"{datetime.now().isoformat()} — Dépôt : +{montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        """Retire un montant si suffisant et positif."""
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"{datetime.now().isoformat()} — Retrait : -{montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def afficher_operations(self):
        print(f"Historique du compte {self.id_compte} :")
        for op in self._operations:
            print(op)


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []  

    def ajouter_compte(self, compte: CompteBancaire):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(f"  Compte {compte.id_compte} — Solde : {compte.get_solde()} €")


if __name__ == "__main__":
    cli = Client("Yassir")
    
    
    compte1 = CompteBancaire()
    compte2 = CompteBancaire(500.0)
    
    cli.ajouter_compte(compte1)
    cli.ajouter_compte(compte2)

    compte1.deposer(300)
    compte1.retirer(50)
    compte2.deposer(200)
    
    
    cli.afficher()
    
    print("\nHistorique des opérations du compte 1 :")
    compte1.afficher_operations()
