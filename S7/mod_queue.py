from queue import Queue

q = Queue(maxsize=4)

print(q.qsize())
q.put(344)
q.put(454)
q.put(765)
q.put(245)
print(q.qsize())
print(f"\nFull: {q.full()}")
print("\nzdejmowanie elementów z kolejki")
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print(f"Kolejka pusta: {q.empty()}")
