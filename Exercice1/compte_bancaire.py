
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire     
        self.__solde = solde_initial   
        self._operations = []           

    def deposer(self, montant):
        """Dépose un montant positif et l'ajoute au solde."""
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        """Retire un montant si suffisant et positif."""
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        """Propriété en lecture seule pour accéder au solde."""
        return self.__solde

    def afficher_operations(self):
        """Affiche l’historique des opérations."""
        print("Historique des opérations :")
        for op in self._operations:
            print(op)

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"



if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    
    try:
        compte.solde = 500
    except AttributeError as e:
        print("Erreur capturée :", e)

    
    compte.afficher_operations()
