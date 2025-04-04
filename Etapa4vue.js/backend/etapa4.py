from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Configuração de CORS para permitir acesso de qualquer origem (*)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode substituir "*" por ["http://localhost:3000"] se quiser restringir ao seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar dados do CSV
df = pd.read_csv("../../arquivos/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")

# Normalizar texto
df = df.fillna("")
df["Razao_Social"] = df["Razao_Social"].str.strip().str.lower()


@app.get("/buscar")
def buscar_operadora(q: str = Query(..., min_length=1)):
    q = q.strip().lower()
    resultados = df[df["Razao_Social"].str.contains(q, case=False, na=False)].fillna("")

    if resultados.empty:
        return {"message": "Nenhuma operadora encontrada."}

    return resultados.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)