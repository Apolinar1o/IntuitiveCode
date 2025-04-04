import requests
import zipfile
import os
from bs4 import BeautifulSoup

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Fazendo a requisição HTTP para acessar o site
response = requests.get(url)

# Verificando se o acesso ao site foi bem-sucedido
if response.status_code == 200:
    print("Acesso realizado")
else:
    print("Falha ao acessar o site")
    exit()  # Encerra o programa se não for possível acessar o site

# Utilizando BeautifulSoup para analisar o HTML da página
soup = BeautifulSoup(response.text, "html.parser")
link_achados = []  # Lista para armazenar os links dos PDFs encontrados

# Procurando os links chamados de anexo_i e anexo_ii
for link in soup.find_all("a", href=True):
    if ("anexo_i" in link["href"].lower() or "anexo_ii." in link["href"].lower()) and ".pdf" in link["href"]:
        link_achados.append(link["href"])  # Adiciona os links encontrados à lista

print(link_achados)

# Criar a pasta onde os arquivos PDF serão armazenados
os.makedirs("../anexos", exist_ok=True)

# Baixar cada arquivo PDF encontrado
for link in link_achados:
    resposta = requests.get(link, stream=True)  # Faz o download do arquivo mantendo o fluxo ativo
    nomeArquivo = os.path.join("../anexos", link.split("/")[-1])  # Define o nome do arquivo a partir do link
    with open(nomeArquivo, "wb") as pdf_file:
        pdf_file.write(resposta.content)  # Salva o conteúdo do PDF no arquivo local
        print(f"Download concluído: {nomeArquivo}")

zip_file_name = "../anexos/anexos_compactados.zip"

# Criando um arquivo ZIP e adicionando os PDFs baixados
with zipfile.ZipFile(zip_file_name, "w") as zipf:
    for root, dirs, files in os.walk("../anexos"):  # Percorre a pasta "anexos"
        for file in files:
            zipf.write(os.path.join(root, file), file)  # Adiciona cada arquivo ao ZIP

print(f"Arquivos compactados com sucesso: {zip_file_name}")