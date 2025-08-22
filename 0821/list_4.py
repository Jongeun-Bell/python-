names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for i, (names,scores) in enumerate(zip(names, scores),1):
    print(f"{i}:학생: {names}, 점수: {scores}")
    