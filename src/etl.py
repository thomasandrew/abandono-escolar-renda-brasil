"""Pipeline reprodutível: preserva valores ausentes, sem imputação arbitrária."""
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

def executar():
    entrada = ROOT / "data/raw/AbandonoEscolar_RendaMedia_2013_2023.csv"
    df = pd.read_csv(entrada, encoding="utf-8")
    df["Ano"] = pd.to_numeric(df["Ano"], errors="raise").astype("int64")
    for coluna in ["Taxa_Abandono", "Renda_Media"]:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    saida = ROOT / "data/processed/dados_limpos.csv.gz"
    saida.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(saida, index=False, compression="gzip")
    print(f"{len(df)} linhas; {df['Taxa_Abandono'].isna().sum()} taxas ausentes; saída: {saida}")
    return df

if __name__ == "__main__":
    executar()
