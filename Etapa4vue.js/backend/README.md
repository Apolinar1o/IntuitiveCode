# API de Busca de Operadoras por Razão Social — FastAPI

Esta aplicação fornece um endpoint de busca textual sobre dados de operadoras de planos de saúde usando FastAPI e Pandas.

---

## ✅ Requisitos

- Python 3.8+
- Pip instalado
- Arquivo `Relatorio_cadop.csv` disponível na pasta `../../arquivos/`

---

## 🔧 Instalação e Execução

```bash: uvicorn etapa4:app --reload --port 8080```

use essa URL POSTMAN: 
```http://127.0.0.1:8080/buscar?q=RAZAO_SOCIAL_DESAJADA```