# Conversor de Moedas - Diogo Teixeira

print("=== Conversor de Moedas ===")

# Dicionário com taxas fictícias
taxas = {
    'USD': 5.10,   # Dólar
    'EUR': 5.50,   # Euro
    'ARS': 0.02,   # Peso Argentino
    'BTC': 250000.00  # Bitcoin (valor simbólico)
}

# Entrada do usuário
valor_brl = float(input("Digite o valor em reais (R$): "))
moeda = input("Digite a moeda de destino (USD, EUR, ARS, BTC): ").upper()

# Verificação e conversão
if moeda in taxas:
    convertido = valor_brl / taxas[moeda]
    print(f"R$ {valor_brl:.2f} equivale a {convertido:.2f} {moeda}")
else:
    print("Moeda não suportada.")
