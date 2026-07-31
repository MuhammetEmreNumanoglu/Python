import statistics

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Stdev:", round(statistics.stdev(data), 2))
print("Variance:", round(statistics.variance(data), 2))
print("Pstdev:", round(statistics.pstdev(data), 2))

print("Median low:", statistics.median_low(data))
print("Median high:", statistics.median_high(data))

scores = [85, 90, 78, 92, 88, 76, 95, 83]
print(f"\nScores: {scores}")
print(f"Average: {statistics.mean(scores):.1f}")
print(f"Spread: {statistics.stdev(scores):.1f}")
