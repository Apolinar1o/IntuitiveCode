# Etapa 2 - Extração de Tabelas de PDF ANS

# A etapa 2 precisa necessariamente da etapa 1 para baixar os arquivos necessários para as tabelas

Este script realiza a leitura do PDF **Anexo I** da ANS, extrai tabelas das páginas, transforma em um DataFrame, salva como CSV e compacta em um `.zip`.

## 🧰 Requisitos

- Python 3.7+
- pip
- PDF do Anexo I baixado (de preferência com nome `Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf`) salvo em `../anexos/`


Será criado um arquivo e ele vai ser compactado

use para rodar ```python etapa3.py ```