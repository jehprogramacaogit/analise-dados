import pandas as pd

def limpar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)

    # Remover valores nulos
    df.dropna(inplace=True)

    # Corrigir tipo de dado
    df['Data'] = pd.to_datetime(df['Data'])

    # Corrigir valores negativos (se houver)
    df = df[df['Quantidade'] > 0]
    df = df[df['Preco_Unitario'] > 0]

    df.to_csv(caminho_csv, index=False)
    print("Dados limpos e salvos!")

if __name__ == "__main__":
    limpar_dados('../data/vendas.csv')
