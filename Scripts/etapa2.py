import pdfplumber
import pandas as pd
import zipfile
path = "../anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

tabelas_extra = []


print("Carregando...")
with pdfplumber.open(path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        tabelas = page.extract_tables()

        for tabela in tabelas:
            df = pd.DataFrame(tabela)
            tabelas_extra.append(df)

dataFrame_final = pd.concat(tabelas_extra, ignore_index=True)
print(dataFrame_final)
print("Arquivo foi transformado em csv")



