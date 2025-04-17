p = 349
x = 0
y = 0
counter = 1
y_coords = set()
ys_map = {}
for x in range(0,p):
    for y in range(0,p):
        if (y**2) % p == (x**3 + 7) % p:
            print(f"{counter}:({x},{y})")
            y_coords.add(y) # getting all distinct y coordinates
            if y in ys_map: # dictionary to show that every y coordinate has three times occurences
                val = ys_map.get(y)
                ys_map[y] = val +1
            else:
                ys_map[y] = 1
            counter += 1
print(f'prime(p)={p} order(n)={counter}')
print(f"distinct y-coordinates: {len(y_coords)}")
print(y_coords)
sorted_tuple = sorted(ys_map.items(), key=lambda x: x[0])
print(sorted_tuple)
