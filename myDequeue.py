import collections

# Create dequeue
double_ended_queue = collections.deque(["Monday", "Tuesday", "Wednesday"])

print("Double ended queue:")
print(double_ended_queue)
print("")

# Append element to right side
double_ended_queue.append("Thursday")
print("Append element to right end:")
print(double_ended_queue)
print("")

# Append element to left side
double_ended_queue.appendleft("Sunday")
print("Append element to left end:")
print(double_ended_queue)
print("")

# Delete element at right end
double_ended_queue.pop()
print("Remove element at right end:")
print(double_ended_queue)
print("")

# Delete element at left end
double_ended_queue.popleft()
print("Remove element at left end:")
print(double_ended_queue)
print("")

# Delete element at left end bc nobody likes Mondays
double_ended_queue.popleft()
print("Remove element at left end:")
print(double_ended_queue)
print("")