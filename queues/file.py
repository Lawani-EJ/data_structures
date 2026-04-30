# Create empty queue
queue = []

# Enqueue (add to rear)
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print("Queue:", queue)

# Dequeue (remove from front)
removed = queue.pop(0)

print("Removed:", removed)
print("Queue now:", queue)