
import requests
import zipfile
import os
from bs4 import BeautifulSoup
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response  = requests.get(url)

if response.status_code == 200:
    print("Aceeso realizado")
else :
    print("Falha no site")
    exit()



soup = BeautifulSoup(response.text, "html.parser")
link_achados = []

for link in soup.find_all("a", href=True):
    if "Anexo I." in link["href"].lower() or "Anexo II." in link["href"].lower():
        link_achados.append((link["href"]))

os.makedirs("anexos", exist_ok=True)

for link in link_achados:
    response = requests.get(pdf_link)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


