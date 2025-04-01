import pdfplumber
import pandas as pd
import zipfile
import os
path = "../anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

tabelas_extra = []

substituicoes = {
    "OD": "Odontológica",
    "AMB": "Ambulatorial"
}

print("Carregando...")
with pdfplumber.open(path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        tabelas = page.extract_tables()

        for tabela in tabelas:
            if tabela in tabelas:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])
                tabelas_extra.append(df)

dataFrame_final = pd.concat(tabelas_extra, ignore_index=True)

dataFrame_final.replace(substituicoes, inplace=True)
print(dataFrame_final)

dataFrame_final.to_csv("teste.csv", index=False, encoding="utf-8-sig")
print("Arquivo foi transformado em csv")

csvNome = "teste.csv"
zipNome = "Teste_Antonio.zip"

if os.path.exists(csvNome):
    with zipfile.ZipFile(zipNome, "w") as zipf:
        zipf.write(csvNome, arcname=os.path.basename((csvNome)))
        print("zip Criado com sucesso")
else:
    print("algo deu errado")


