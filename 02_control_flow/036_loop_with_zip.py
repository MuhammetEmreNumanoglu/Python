names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

cities = ["London", "Paris", "Tokyo"]
countries = ["UK", "France", "Japan"]
populations = [9_000_000, 2_100_000, 14_000_000]

for city, country, pop in zip(cities, countries, populations):
    print(f"{city}, {country}: {pop:,}")

pairs = list(zip(names, scores))
print(pairs)
