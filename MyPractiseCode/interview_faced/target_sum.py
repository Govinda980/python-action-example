arr = [1, 2, 5, 3, 7, 5]
target = 12
seen = set()

for item in arr:
    comp = target - item
    if comp in arr:
        seen.add(item)

print(seen)
