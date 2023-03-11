#Victor Gabriel Cunha Rodrigues and Lorrana Evelyn de Aráujo Pereira

import csv

class Drogas:
    def __init__(self, arquivoCSV):
        self.arquivoCSV = arquivoCSV

    def quantidadePorUso(self, age, coluna):
        with open(self.arquivoCSV) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            nome_coluna = header[coluna]
            n_coluna = header.index("n")#descobrir o índice da coluna "n"
            for linha in csv_reader:
                if linha[0] == age:
                    return (linha[n_coluna]), nome_coluna
        return 'erro!'
    
    def drogaMaisUsadaPorIdade(self):
        with open(self.arquivoCSV) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            drogas_por_idade = {}
            for row in csv_reader:
                idade = row[0]
                drogas = max(row[1:])
                index = row.index(max(row[1:]))
                nome_droga = header[index]
                if idade not in drogas_por_idade:
                    drogas_por_idade[idade] = nome_droga
                else:
                    #a nova droga é colocada como valor para a chave da faixa etária no dicionário.
                    if float(drogas) > float(drogas_por_idade[idade]):
                        drogas_por_idade[idade] = nome_droga
            return drogas_por_idade

    

csv1 = Drogas('drug-use-by-age.csv')
print(csv1.quantidadePorUso('13',2))
print(csv1.quantidadePorUso('15',9))

print("Drogas mais usadas por idade:")
drogas_por_idade = csv1.drogaMaisUsadaPorIdade()
for idade, drogas in drogas_por_idade.items():
        print(f"{idade}: {drogas}")
