from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from typing import List

# Inicializando o FastAPI
app = FastAPI()

# Carregando o CSV para o Pandas
# Você pode atualizar o caminho do arquivo conforme necessário
df_operadoras = pd.read_csv('../arquivos/Relatorio_cadop.csv', delimiter=';', encoding='utf-8')


# Definindo um modelo de dados para a busca
class BuscaRequest(BaseModel):
    termo: str


@app.get("/")
def read_root():
    return {"message": "API para busca de operadoras"}


@app.post("/buscar")
def buscar_operadoras(request: BuscaRequest):
    termo = request.termo.lower()

    # Realiza a busca no DataFrame e retorna as operadoras relevantes
    resultado = df_operadoras[df_operadoras['razao_social'].str.contains(termo, case=False, na=False)]

    # Retorna os 10 primeiros resultados
    return {
        "resultados": resultado[['razao_social', 'registro_ans', 'cidade', 'uf']].head(10).to_dict(orient='records')}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)