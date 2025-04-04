from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Carregar dados do CSV
df = pd.read_csv("../arquivos/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")

# Limpeza de dados
df["Nome_Fantasia"] = df["Nome_Fantasia"].fillna("")  # Preencher NaN com string vazia
df["Nome_Fantasia"] = df["Nome_Fantasia"].astype(str).str.strip().str.lower()  # Normalizar texto

@app.get("/buscar")
def buscar_operadora(q: str = Query(..., min_length=1)):
    print(q)
    q = q.strip().lower()
    print(df["Nome_Fantasia"].str.contains(q, case=False, na=False))
    resultados = df[df["Nome_Fantasia"].str.contains(q, case=False, na=False)]
    print("11111111111111111111111111 ", resultados)
    return resultados.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)