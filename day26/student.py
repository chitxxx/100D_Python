import random

students = [f"Name {i}" for i in range(10)]
results = {i: random.randint(1, 100) for i in students}
print(results)

print ({name:score for (name, score) in results.items()})