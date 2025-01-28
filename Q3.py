import json

json_file = "/home/ivanilson-ferreira/Desktop/target/data/dados.json"

with open(json_file, 'r') as file:
    data = json.load(file)

revenues = [day['valor'] for day in data if day['valor'] > 0]

min_revenue = min(revenues)
max_revenue = max(revenues)
average_revenue = sum(revenues) / len(revenues)
days_above_average = sum(1 for value in revenues if value > average_revenue)

print(f"Menor valor de faturamento: {min_revenue}")
print(f"Maior valor de faturamento: {max_revenue}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {days_above_average}")
