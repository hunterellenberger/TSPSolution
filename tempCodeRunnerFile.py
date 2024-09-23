permutations_compute(dfs, distances, coordinates)
for key in distances:
    print(f"{key}: {distances[key]}")
bestRoute = min(distances.keys())
print(bestRoute)