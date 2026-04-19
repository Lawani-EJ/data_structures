# SIMPLE QUEUE EXAMPLE USING LIST

# Create empty queue
queue = []

# Add items to queue (enqueue)
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

# Queue now:
# ["Task 1", "Task 2", "Task 3"]

print("Current Queue:", queue)


# Remove first item (dequeue)
removed_item = queue.pop(0)

# pop(0) removes item at index 0
# index 0 = first item

print("Removed:", removed_item)


# Queue after removal
print("Queue Now:", queue)