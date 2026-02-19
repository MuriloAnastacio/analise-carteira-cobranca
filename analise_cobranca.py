import pandas as pd

# Simulação de carteira de cobrança
dados = {
    "Cliente": ["Empresa A", "Empresa B", "Empresa C", "Empresa D"],
    "Valor": [5000, 12000, 3000, 8000],
    "Dias_Atraso": [10, 45, 5, 90]
}

df = pd.DataFrame(dados)

# Classificação de atraso (Aging List)
def classificar_atraso(dias):
    if dias <= 30:
        return "0-30"
    elif dias <= 60:
        return "31-60"
    else:
        return "61+"

df["Faixa_Atraso"] = df["Dias_Atraso"].apply(classificar_atraso)

# Total em atraso
total_atraso = df["Valor"].sum()

print("Carteira de Cobrança")
print(df)
print("\nTotal em atraso:", total_atraso)

