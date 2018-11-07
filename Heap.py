import heapq

# Create heap
H = [21, 1, 45, 78, 3, 5]
heapq.heapify(H)
print("Printing the created heap:")
print(H)
print()

# Insert element using heappush (added at the end by default)
heapq.heappush(H, 8)
print("Inserting new element at end of heap:")
print(H)
print()

# Removing from the heap
heapq.heappop(H)
print("Removing first element from the heap:")
print(H)
print()

# Replacing smallest element (default behavior)
print("Original heap:")
original = [21, 1, 45, 78, 3, 5]
print(original)
print()
print("Replacing smallest element:")
heapq.heapreplace(H, 6)
print(H)