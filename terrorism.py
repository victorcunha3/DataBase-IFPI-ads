#Victor Gabriel Cunha Rodrigues and Lorrana Evelyn de Aráujo Pereira
import numpy as np

class DataBase:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def total_incidentes(self):
        # Carrega o arquivo CSV em um array NumPy
        data = np.genfromtxt(self.arquivo, delimiter=',', dtype=str)

        # Filtra as linhas com valores numericos e converte para um array de inteiros
        incidentes = data[:, 1]
        mask = np.char.isdigit(incidentes)#apenas as linhas com valores numericos
        incidentes = incidentes[mask].astype(int)

        # Soma os valores dos incidentes
        total_incidents = np.sum(incidentes)
        print("Total de incidentes:", total_incidents)
    
    def KilledPerCountry(self):
        d = np.genfromtxt(self.arquivo, delimiter=',',dtype = str)
        killed = d[:,3]
        mask = np.char.isdigit(killed)
        killed = killed[mask].astype(int)

        all_killed = np.sum(killed)
        print ("Total de mortos:",all_killed)


a = DataBase('country_stats_1993_appendix2.csv')
a.total_incidentes()
a.KilledPerCountry()
