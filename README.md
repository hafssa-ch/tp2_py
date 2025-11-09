# TP 2 : Classes, Encapsulation et Composition

Ce TP a pour objectif de pratiquer l’encapsulation et la composition de classes en Python.
Les exercices montrent comment sécuriser l’accès aux données, gérer des opérations bancaires et représenter des relations « un à plusieurs » entre objets.

## Exercice 1 — Compte Bancaire

### Objectif pédagogique :
Appliquer les principes d’encapsulation en Python :
Attributs protégés et privés (_attribut et __attribut)
Propriétés (@property)
Validation des données
Séparation interface / données internes

### Description :
Classe CompteBancaire avec _titulaire (protégé) et __solde (privé).
Méthodes deposer(montant) et retirer(montant) avec contrôle de validité.
Propriété solde en lecture seule pour empêcher toute modification directe.
Historique des opérations dans _operations.

### Exemple d’utilisation :
compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)
print(compte)
print("Solde accessible :", compte.solde)
compte.afficher_operations()


## Résultat attendu :
<img width="947" height="148" alt="image" src="https://github.com/user-attachments/assets/121597aa-9321-4af2-a668-b77ef0e7ecb5" />



## Exercice 2 — Client et Compte Bancaire (Composition)

### Objectif pédagogique :
Mettre en œuvre l’association entre classes via composition. Une classe peut utiliser une autre sans héritage, illustrant une relation « a un » ou « utilise ».

### Description :
Classe Client avec nom et une liste de comptes comptes.
Classe CompteBancaire déjà implémentée (avec encapsulation du solde et historique).
Méthode afficher() dans Client pour afficher le nom du client et le solde de tous ses comptes.
Possibilité de gérer plusieurs comptes par client et de générer l’historique des opérations horodaté.

### Exemple d’utilisation :
cli = Client("Yassir")
compte1 = CompteBancaire()
compte2 = CompteBancaire(500)
cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)

compte1.deposer(300)
compte1.retirer(50)
compte2.deposer(200)

cli.afficher()
compte1.afficher_operations()


### Résultat attendu :
<img width="620" height="237" alt="image" src="https://github.com/user-attachments/assets/de0e0c32-4889-4081-9d0a-dc3a35212e8f" />
