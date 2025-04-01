
import requests
import zipfile
import os
from bs4 import BeautifulSoup
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response  = requests.get(url)

if response.status_code == 200:
    print("Acesso realizado")
else :
    print("Falha no site")
    exit()


soup = BeautifulSoup(response.text, "html.parser")
link_achados = []


for link in soup.find_all("a", href=True):
    if ("anexo_i" in link["href"].lower() or "anexo_ii." in link["href"].lower()) and ".pdf" in link["href"]:
        link_achados.append((link["href"]))

print(link_achados)

os.makedirs("../anexos", exist_ok=True)

for link in link_achados:
    resposta = requests.get(link, stream=True)
    nomeArquivo = os.path.join("../anexos", link.split("/")[-1])
    with open(nomeArquivo, "wb") as pdf_file:
        pdf_file.write(resposta.content)
        print("Download feito")



zip_file_name = "../anexos/anexos_compactados.zip"
with zipfile.ZipFile(zip_file_name, "w") as zipf:
    for root, dirs, files in os.walk(""):
        for file in files:
            zipf.write(os.path.join(root, file), file)


