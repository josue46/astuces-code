import csv
import os.path
import os

class FormatData:
    def __init__(self, name="", age=0, married=False):
        self.name = name
        self.age = age
        self.married = married

    
    def __str__(self):
        outstring = "'{0}', {1}, {2}".format(self.name, self.age, self.married)
        return outstring 


    def savedata(filename="", datalist=[]):
        """This function saving data in a csv file"""
        with open(filename, "w", newline="\n") as csvfile:
            DataWriter = csv.writer(
                csvfile,
                delimiter="\n",
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            DataWriter.writerow(datalist)
            csvfile.close()
            print("Données enrégistré")


    def read_data(filename=""):
        """This function read data in a csv file"""
        with open(filename, 'r', newline='\n') as csvfile:
            DataReader = csv.reader(
                csvfile,
                delimiter="\n",
                quotechar=" ", 
                quoting=csv.QUOTE_NONNUMERIC)
            for datareader in DataReader:
                print(", ".join(datareader))
            csvfile.close()
            print("Les données ont été lues avec succès !")
    

    def add_data(filename="", DataAdd=""):
        """This function add data in a csv file"""
        if not os.path.isfile(filename):
            print("Le fichier où vous essayez d'ajouter vos données n'existe pas sur ce disque !")
            quit()

        newdata = []
        data = DataAdd
        newdata.append(data)
        with open(filename, 'a', newline='\n') as csvfile:
            ecrire = csv.writer(csvfile, delimiter="\n", quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)
            ecrire.writerow(newdata)
            csvfile.close()
        print("Les données ont bien été ajouté !")
    

    def delete_file(filename=""):
        """This function delete the file in a directory"""
        if not os.path.isfile(filename):
            print("Le fichier que vous essayez de supprimer est introuvable ou n'existe pas dans votre disque !")
            quit()
        
        os.remove(filename)
        print("Fichier supprimé !")


    def remove_data(file="", dataname=""):
        if not os.path.isfile(file):
            print("Le Fichier que vous essayez d'ouvrir n'existe pas dans votre disque !")
        
        with open(file, 'r', newline='\n') as csvfile:
            lire = csv.reader(csvfile)