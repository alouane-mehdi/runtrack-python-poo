class student:
    def __init__(self,nom,prénom,NumeroEtudiant):
        self.nom=nom
        self.prenom=prénom
        self.NumeroEtudiant=NumeroEtudiant
        self.Credit=0
        self.level=self.studentEval()
    def add_credit(self, credit):
        if credit >0:
            self.Credit += credit
        else :
            print("Erreur : Le montant est négatif")
    def NombreCredit(self):
        print(f"Le nombre de crédit de {self.prenom} {self.nom} est de {self.Credit} points")
    def studentEval(self):
        if self.Credit >= 90:
            return "Excellent"
        elif self.Credit >= 80:
            return "Très bien"
        elif self.Credit >= 70:
            return "Bien"
        elif self.Credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def studentInfo(self):
        print(f"Nom : {self.nom} \nPrénom : {self.prenom} \nId : {self.NumeroEtudiant} \nNiveau : {self.studentEval()}")
etudiant1=student("Doe", "John", 145)
etudiant1.add_credit(73)
etudiant1.NombreCredit()
etudiant1.studentInfo()