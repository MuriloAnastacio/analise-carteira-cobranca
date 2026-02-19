import pandas as pd

# Ler dados
df = pd.read_csv("dados/carteira.csv")

# Classificar atraso
def classificar_atraso(dias):
    if dias <= 30:
        return "0-30"
    elif dias <= 60:
        return "31-60"
    elif dias <= 90:
        return "61-90"
    else:
        return "90+"

df["faixa_atraso"] = df["dias_atraso"].apply(classificar_atraso)

# Indicadores
total_divida = df["valor"].sum()
media_atraso = df["dias_atraso"].mean()

print("Total da carteira:", total_divida)
print("Média de atraso:", media_atraso)
print(df)
