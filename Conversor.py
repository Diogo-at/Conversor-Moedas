print("=== Conversor de Moedas ===")

# Dicionário com taxas fictícias em relação ao real (BRL)
taxas = {
    'BRL': 1.00,       # Real
    'USD': 5.10,       # Dólar
    'EUR': 5.50,       # Euro
    'ARS': 0.02,       # Peso Argentino
    'BTC': 250000.00   # Bitcoin (valor simbólico)
}

# Mostrar opções disponíveis
print("Moedas disponíveis:", ", ".join(taxas.keys()))

try:
    # Entrada das moedas
    moeda_origem = input("Digite a moeda de origem: ").strip().upper()
    moeda_destino = input("Digite a moeda de destino: ").strip().upper()

    if moeda_origem in taxas and moeda_destino in taxas:
        valor = float(input(f"Digite o valor em {moeda_origem}: "))

        # Conversão: primeiro para BRL, depois para moeda de destino
        valor_em_brl = valor * taxas[moeda_origem]
        convertido = valor_em_brl / taxas[moeda_destino]

        print(f"\n{valor:.4f} {moeda_origem} equivale a {convertido:.4f} {moeda_destino}")
    else:
        print("Uma ou ambas as moedas digitadas não são suportadas.")

except ValueError:
    print("Valor inválido! Digite um número.")
