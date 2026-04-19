### Queues
Ques are data structures that store elements of data followin the F.I.F.O policy all additions are made at the rear of the queue and all deletions are made at the front of the queue

#### Diagram

```text
Enqueue (Add at Rear)  ----->

Front                       Rear
  ↓                          ↓
+---------+---------+---------+
| Task 1  | Task 2  | Task 3  |
+---------+---------+---------+

Dequeue (Remove from Front)
Removes: Task 1
```

``` python
queue = []

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print("Current Queue:", queue)

removed_item = queue.pop(0)
print("Removed:", removed_item)

print("Queue Now:", queue)

```