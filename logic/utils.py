# Comparação dos resultados extraídos pelo programa com os dados referência (do mestrado)

## Formato dados referência: 
    ### Começa na linha 3, coluna 1: nome, coluna 4: núcleos +, coluna 5: núcleos
    ### Coluna 6: total de núcleos, coluna 9: % de N+
## Formato dados extraídos:
    ### Coluna 1: nome, coluna 2: núcleos +, coluna 3: núcleos -, coluna 4: total de núcleos, coluna 5: porcentagem +

import pandas as pd
import os

# Obtém o diretório atual do notebook
current_dir = os.getcwd()

# Volta uma pasta para o diretório onde estão os dados
# Certifique-se de que a estrutura de diretórios esteja correta
data_path = os.path.abspath(os.path.join(current_dir, 'grupyum/grupyum', '..', 'data/data'))

# Define os caminhos dos arquivos
reference_path = os.path.join(data_path, "tma5.xlsx")
extracted_path = os.path.join(data_path, "resultsTMA5.xlsx")

def compare(reference_path, extracted_path):

    # Carregar os dados extraídos
    extracted_data = pd.read_excel(extracted_path, header=0, usecols=[0, 1, 2, 3, 4], names=["Name", "Nuclei+", "Nuclei-", "Total Nuclei", "Percentage+"])
    extracted_data["Name"] = extracted_data["Name"].apply(lambda x: x[:7] + '...' if len(x) > 7 else x)
    print("\nDados extraídos:")
    print(extracted_data)
    extracted_rows, extracted_cols = extracted_data.shape
    
    # Carregar os dados de referência
    reference_data = pd.read_excel(reference_path, header=None, skiprows=1, usecols=[0, 3, 4, 5, 8], names=["Name", "Nuclei+", "Nuclei-", "Total Nuclei", "Percentage+"])
    print("Dados de referência:")
    reference_data = reference_data[:extracted_rows]
    print(reference_data)

    # Converter as colunas selecionadas para numérico
    for column in ["Nuclei+", "Nuclei-", "Total Nuclei", "Percentage+"]:
        reference_data[column] = pd.to_numeric(reference_data[column], errors='coerce')
        extracted_data[column] = pd.to_numeric(extracted_data[column], errors='coerce')

    # Criar um DataFrame com as diferenças
    comparison = pd.DataFrame({
    "Name": reference_data["Name"],
    "Df Nuclei+": (extracted_data["Nuclei+"] - reference_data["Nuclei+"]),
    "Df Nuclei-": (extracted_data["Nuclei-"] - reference_data["Nuclei-"]),
    "Df Total Nuclei": abs(reference_data["Total Nuclei"] - extracted_data["Total Nuclei"]),
    "Df Percentage+": abs(reference_data["Percentage+"] - extracted_data["Percentage+"]),
    "Rltv error %": [
        0 if (ref == 0 or ext == 0) else 
        abs(((ext - ref) / max(ref, ext)) * 100)
        for ref, ext in zip(reference_data["Percentage+"], extracted_data["Percentage+"])
        ]
    })

    # Exibir os resultados da comparação
    # print("\nResultados da comparação:")
    # print(comparison)

    return comparison

comp = compare(reference_path, extracted_path)
print(comp)
