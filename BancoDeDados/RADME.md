# 📊 Banco de Dados SQL - Intuitive

Este módulo SQL é responsável por:

- Criar e estruturar o banco de dados `intuitive`
- Carregar dados das operadoras da ANS e suas demonstrações contábeis (CSV)
- Realizar análises para identificar as 10 operadoras com maiores despesas

---

## 🗃️ Estrutura do Banco

- **Banco**: `intuitive`
- **Tabelas**:
  - `operadoras`: dados cadastrais das operadoras
  - `demonstracoes_contabeis`: dados financeiros trimestrais das operadoras





## Configuração do MySQL para permitir importação
Antes de carregar os arquivos CSV, é necessário desabilitar temporariamente a proteção contra atualizações inseguras:
e em caso de erro de permissão mudar a configuração secure_file_priv para aceitar a pasta do arquivo que você vai fazer o loading


```SET SQL_SAFE_UPDATES = 0;```

``` LOAD DATA LOCAL INFILE 'CAMINHO_COMPLETO/Relatorio_cadop.csv'```

no arquivo Etapa3.sql tem o arquivo usado por mim, necessário mudar o caminho dos arquivos em testes