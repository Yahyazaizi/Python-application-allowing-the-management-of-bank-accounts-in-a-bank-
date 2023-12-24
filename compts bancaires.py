import csv
import random


class CompteBancaire:
    _nober = 1

    def __init__(self, solde):
        self.solde = solde
        CompteBancaire._nober += 1
        self.numero_de_compte = self.numero_du_comptr(CompteBancaire._nober)

    def deposer(self, somme):
        self.solde += somme

    def retirer(self, somme):
        if somme > self.solde:
            return "Erreur"
        else:
            self.solde -= somme

    def numero_du_comptr(self, n):
        return str(CompteBancaire._nober) + str(random.randint(1, 100))


class client(CompteBancaire):
    _nober = 1

    def __init__(self, solde, mot_de_pass):
        super().__init__(solde)
        self.mot_de_pass = mot_de_pass
        CompteBancaire._nober += 1

        self.numero_de_compte = numero_de_compte

    def deposer(self, somme):
        self.solde += somme

    def retirer(self, somme):
        if somme > self.solde:
            return "Erreur"
        else:
            self.solde -= somme


# New dictionary to store client information
ClientCompte = { }

# 3. Définir la fonction lambda genererNumCompte
genererNumCompte = lambda client_num: client_num + 1000


# 4. Ecrire une fonction EcrireFichierCSV
def EcrireFichierCSV(client_dict, filename='clients.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ClientNum', 'AccountNum', 'Password'])
        for client_num, (account_num, password) in client_dict.items():
            writer.writerow([client_num, account_num, password])


# 5. Ecrire une fonction manipSTS
def manipSTS(client_dict):
    num_list = list(client_dict.values())
    num_tuple = tuple(client_dict.values())
    num_set = set(client_dict.values())
    return num_list, num_tuple, num_set
def numero_du_comptr(_nober):
    return str(CompteBancaire._nober) + str(random.randint(1, 100))

n = int(input("Entrez le nombre de clients: "))
t = []





for i in range(n):
    numero_de_compte = print("numero_de_compte:", str(CompteBancaire._nober) + str(random.randint(1, 100)))
    solde = int(input("Entrez le solde: "))
    mot_de_pass = input("Entrez le mot_de_pass: ")
    t1 = client(solde, mot_de_pass)
    t.append(t1)

# 6. Ecrire un programme principal

while True:
    print("Menu:")
    print("1. Ajouter un Compte")
    print("2. Supprimer un Compte")
    print("3. Modifier son mot de passe")
    print("4. Afficher son solde")
    print("5. Déposer une somme d’argent")
    print("6. Retirer une somme d’argent")
    print("7. Enregistrer les numéros des clients dans un fichier CSV")
    print("8. Créer une liste, un tuple et un set de numéros de comptes")
    print("9. Quitter")

    x = int(input("Entrez votre choix: "))

    if x == 1:
        numero_de_compte = print("numero_de_compte:", str(CompteBancaire._nober) + str(random.randint(1, 100)))
        solde = int(input("Entrez le solde: "))
        mot_de_pass = input("Entrez le mot de passe: ")
        t= client(solde, mot_de_pass)
        ClientCompte[CompteBancaire._nober] = (t.numero_de_compte, t.mot_de_pass)


    elif x == 2:
        solde = int(input("Entrez le solde: "))
        mot_de_pass = input("Entrez le mot_de_pass: ")
        for i in range(n):
            if solde == t[i].solde and mot_de_pass == t[i].mot_de_pass:
                del t[i]
                n -= 1
                i -= 1

    elif x == 3:
        mot_de_pass = input("Entrez le mot de passe puis devient modifié: ")
        for i in range(n):
            if mot_de_pass == t[i].mot_de_pass:
                t[i].mot_de_pass = input("Entrez le nouveau mot de passe: ")

    elif x == 4:
        [print(obj.solde) for obj in t]

    elif x == 5:
        mot_de_pass = input("Entrez le mot de passe puis devient modifié: ")
        for client in t:
            client.deposer(int(input("Entrez le montant à déposer: ")))
            print("La somme a été déposée avec succès.")
            break

    elif x == 6:
        mot_de_pass = input("Entrez le mot de passe puis devient modifié: ")
        for client in t:
            client.retirer(int(input("Entrez le montant à retirer: ")))
            
            break

    elif x == 7:
        EcrireFichierCSV(ClientCompte)
        print("Les numéros des clients ont été enregistrés dans le fichier CSV.")

    elif x == 8:
        num_list, num_tuple, num_set = manipSTS(ClientCompte)
        print("Liste de numéros de comptes:", num_list)
        print("Tuple de numéros de comptes:", num_tuple)
        print("Set de numéros de comptes:", num_set)

    elif x == 9:
        print("Programme terminé.")
        break

    else:
        print("Choix invalide. Veuillez choisir à nouveau.")
