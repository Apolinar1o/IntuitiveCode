import pdfplumber
import pandas as pd
import zipfile
import os

path = "../anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Lista para armazenar todas as tabelas extraídas do PDF
tabelas_extra = []

# Dicionário para substituir abreviações nas colunas
substituicoes = {
    "OD": "Odontológica",
    "AMB": "Ambulatorial"
}

print("Carregando o PDF...")

# Abre o arquivo PDF e percorre todas as páginas
with pdfplumber.open(path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        # Extrai
        tabelas = page.extract_tables()

        # Processa cada tabela encontrada na página
        for tabela in tabelas:
            if tabela:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])  # Ajusta o cabeçalho corretamente
                tabelas_extra.append(df)

# junta tudo em um unico dataFrame
dataFrame_final = pd.concat(tabelas_extra, ignore_index=True)

# Substitui as abreviações OD e AMB pelas descrições completas
dataFrame_final.replace(substituicoes, inplace=True)


print("Tabela extraída:")
print(dataFrame_final)


csvNome = "teste.csv"

# Salva os dados extraídos em formato CSV
dataFrame_final.to_csv(csvNome, index=False, encoding="utf-8-sig")
print(f"Arquivo CSV criado: {csvNome}")

zipNome = "Teste_Antonio.zip"

# compacta
if os.path.exists(csvNome):
    with zipfile.ZipFile(zipNome, "w") as zipf:
        zipf.write(csvNome, arcname=os.path.basename(csvNome))  # Adiciona corretamente o CSV ao ZIP
        print(f"Arquivo ZIP criado com sucesso: {zipNome}")
else:
    print("Erro: O arquivo CSV não foi encontrado e não pode ser compactado.")