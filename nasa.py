
print("NASA DATA STATISTICS")
print("====================")

# Planet selection
planets = ["mercury", "venus", "earth", "mars",
           "jupiter", "saturn", "uranus", "neptune"]

for attempt in range(2):
    print("\nPlanets:", ", ".join(p.capitalize() for p in planets))
    planet = input("Select planet: ").strip().lower()

    if planet in planets:
        break
    print("Invalid planet!")

else:
    planet = "mars"
    print("Default planet: Mars")

planet = planet.capitalize()
print("\nAnalyzing:", planet)

# Temperature input
temps = []

for day in range(1, 6):
    while True:
        try:
            temps.append(float(input(f"Day {day}: ")))
            break
        except ValueError:
            print("Enter a valid number!")

# Statistics
mean = sum(temps) / 5
sorted_temps = sorted(temps)
median = sorted_temps[2]
highest = max(temps)
lowest = min(temps)

print("\n===== STATISTICS =====")
print("Planet:", planet)
print("Mean:", round(mean, 2))
print("Median:", median)
print("Range:", highest - lowest)
print("Hottest day:", temps.index(highest) + 1)
print("Coldest day:", temps.index(lowest) + 1)

# Sorted data
print("\n===== SORTED DATA =====")
for t in sorted_temps:
    print(t)

# Temperature graph
print("\n===== TEMPERATURE GRAPH =====")
for i, t in enumerate(temps, 1):
    bars = "#" * max(0, int((t + 100) / 2))
    print(f"Day {i} | {bars} {t} C")

# Daily changes
print("\n===== TEMPERATURE CHANGES =====")
for i in range(1, 5):
    change = temps[i] - temps[i-1]
    status = "increased" if change > 0 else "decreased" if change < 0 else "stable"
    symbol = "+" if change > 0 else "-"
    print(f"Day {i} to {i+1}: {change} C ({status})")
    print("Jump:", symbol * int(abs(change) / 2))

# Temperature analysis
print("\n===== TEMPERATURE ANALYSIS =====")

if mean < -50:
    print("Status: FREEZING")
elif mean < 0:
    print("Status: VERY COLD")
elif mean <= 30:
    print("Status: MODERATE")
elif mean <= 60:
    print("Status: HOT")
else:
    print("Status: EXTREME HEAT")

print("Note: Temperature alone cannot determine habitability.")

# Prediction
print("\n===== DAY 7 PREDICTION =====")

trend = (temps[-1] - temps[0]) / 4
day6 = temps[-1] + trend
day7 = day6 + trend

if trend > 0:
    print("Trend: WARMING")
elif trend < 0:
    print("Trend: COOLING")
else:
    print("Trend: STABLE")

print("Daily trend:", round(trend, 2), "C")
print("Day 6:", round(day6, 2), "C")
print("Day 7:", round(day7, 2), "C")

# Average comparison
print("\n===== AVERAGE ANALYSIS =====")
print("Average:", round(mean, 2), "C")

if day7 > mean:
    print("Day 7: WARMER than average")
elif day7 < mean:
    print("Day 7: COLDER than average")
else:
    print("Day 7: EQUAL to average")

print("\nAnalysis completed!")
print("====================")
print("Independent Student Researcher")
